# Original Bioconductor VIPER on real centered donor x cell-type pseudobulk.
# Run from repository root: Rscript methods/viper/run_viper.R
args <- commandArgs(trailingOnly = TRUE)
repo <- if (length(args)) normalizePath(args[1], winslash = "/") else normalizePath(".", winslash = "/")
if (!requireNamespace("viper", quietly = TRUE)) stop("Bioconductor viper is required in an isolated R library")
if (!requireNamespace("jsonlite", quietly = TRUE)) stop("jsonlite is required")
analysis <- jsonlite::fromJSON(file.path(repo, "config", "analysis.json"))
expression_path <- file.path(repo, "data", "local", "pseudobulk_centered.csv.gz")
prior_path <- file.path(repo, "data", "cache", "collectri.csv")
if (!file.exists(expression_path) || !file.exists(prior_path)) stop("Actual pseudobulk and curated prior files are required")
pb <- read.csv(gzfile(expression_path), row.names = 1, check.names = FALSE)
eset <- t(as.matrix(pb))
storage.mode(eset) <- "double"
stopifnot(ncol(eset) > 1, !anyDuplicated(rownames(eset)), !anyDuplicated(colnames(eset)), all(is.finite(eset)))
prior <- read.csv(prior_path, check.names = FALSE)
stopifnot(all(c("source", "target", "weight") %in% names(prior)))
stopifnot(!anyDuplicated(prior[c("source", "target")]))
original_edges <- nrow(prior)
prior <- prior[prior$target %in% rownames(eset) & is.finite(prior$weight) & prior$weight != 0, ]
regulon <- lapply(split(prior, prior$source), function(x) {
  list(tfmode = setNames(sign(x$weight), x$target), likelihood = setNames(rep(1, nrow(x)), x$target))
})
regulon <- regulon[vapply(regulon, function(x) length(x$tfmode), integer(1)) >= analysis$min_targets]
if (!length(regulon)) stop("No TF prior passes configured min_targets")
parameters <- list(method = "none", minsize = analysis$min_targets, eset.filter = FALSE, pleiotropy = analysis$viper_pleiotropy, cores = 1,
  verbose = FALSE, nes = TRUE, bootstraps = 0, likelihood = "Uniform 1 per retained target", tfmode = "Sign of CollecTRI weight")
set.seed(analysis$seed)
start <- proc.time()[["elapsed"]]
activity <- viper::viper(eset, regulon, method = "none", minsize = analysis$min_targets, eset.filter = FALSE,
  pleiotropy = analysis$viper_pleiotropy, cores = 1, verbose = FALSE)
elapsed <- proc.time()[["elapsed"]] - start
stopifnot(all(is.finite(activity)), identical(colnames(activity), colnames(eset)))
output <- data.frame(sample = colnames(activity), t(activity), check.names = FALSE)
dir.create(file.path(repo, "results", "tables"), recursive = TRUE, showWarnings = FALSE)
write.csv(output, file.path(repo, "results", "tables", "bioc_viper_activity_matrix.csv"), row.names = FALSE)
runtime <- list(status = "executed", software = "Original Bioconductor VIPER", version = as.character(packageVersion("viper")),
  R_version = R.version.string, seed = analysis$seed, parameters = parameters, elapsed_seconds = elapsed,
  input = list(expression = "data/local/pseudobulk_centered.csv.gz", prior = "data/cache/collectri.csv",
    expression_md5 = unname(tools::md5sum(expression_path)), prior_md5 = unname(tools::md5sum(prior_path)),
    genes = nrow(eset), samples = ncol(eset), original_prior_edges = original_edges,
    matched_prior_edges = nrow(prior), scored_regulators = nrow(activity)),
  output = list(path = "results/tables/bioc_viper_activity_matrix.csv", orientation = "sample x regulator", finite = TRUE),
  packages = setNames(lapply(c("viper", "Biobase", "BiocGenerics", "mixtools", "e1071", "proxy", "KernSmooth", "jsonlite"), function(p) as.character(packageVersion(p))),
    c("viper", "Biobase", "BiocGenerics", "mixtools", "e1071", "proxy", "KernSmooth", "jsonlite")),
  limitations = c("Curated prior; ARACNe de novo inference was not executed.", "No msVIPER/MRA was executed.",
    "Donor group mapping and assay confounding limit disease interpretation.", "Original VIPER output is distinct from decoupler's VIPER implementation."))
jsonlite::write_json(runtime, file.path(repo, "methods", "viper", "R_runtime.json"), auto_unbox = TRUE, pretty = TRUE)
writeLines(capture.output(sessionInfo()), file.path(repo, "methods", "viper", "sessionInfo.txt"))
cat("Original VIPER executed: ", ncol(activity), " samples x ", nrow(activity), " regulators; ", round(elapsed, 2), " seconds\n", sep = "")
