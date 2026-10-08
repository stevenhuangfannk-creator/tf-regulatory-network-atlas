# Real-data-only figure pipeline. Run from repository root with Rscript scripts/plot_atlas.R.
args <- commandArgs(trailingOnly = TRUE)
repo <- if (length(args)) normalizePath(args[1], winslash = "/") else normalizePath(".", winslash = "/")
needed <- c("ggplot2", "patchwork", "svglite", "ragg", "ggrastr", "jsonlite")
missing <- needed[!vapply(needed, requireNamespace, logical(1), quietly = TRUE)]
if (length(missing)) stop("Missing R plotting packages: ", paste(missing, collapse = ", "))
library(ggplot2)
library(patchwork)
cfg <- jsonlite::fromJSON(file.path(repo, "config", "figure_contract.json"), simplifyVector = FALSE)
analysis <- jsonlite::fromJSON(file.path(repo, "config", "analysis.json"))
set.seed(analysis$seed)
tabdir <- file.path(repo, "results", "tables")
outdir <- file.path(repo, "results", "figures")
dir.create(outdir, recursive = TRUE, showWarnings = FALSE)
read_result <- function(name, required) {
  path <- file.path(tabdir, name)
  if (!file.exists(path)) stop("Real result table is missing: ", path)
  z <- read.csv(if (grepl("gz$", name)) gzfile(path) else path, check.names = FALSE)
  if (!all(required %in% names(z)) || !nrow(z)) stop("Invalid real result table: ", name)
  z
}
cells <- read_result("cells.csv.gz", c("cell_id", "donor", "condition", "cell_type", "umap_1", "umap_2"))
pb <- read_result("pseudobulk_activity.csv", c("sample", "donor", "condition", "cell_type", "tf", "method", "score", "n_cells"))
diff <- read_result("differential_activity.csv", c("cell_type", "tf", "method", "effect", "ci_low", "ci_high", "pvalue", "fdr", "n_healthy", "n_disease"))
edges_all <- read_result("selected_network_edges.csv", c("source", "target", "weight", "evidence_type", "references", "target_logcpm_change"))
profile <- read_result("celltype_activity.csv", c("cell_type", "condition", "tf", "mean_activity", "mean_expression", "n_cells"))
conc <- read_result("method_concordance.csv", c("cell_type", "tf", "ulm_effect", "viper_effect", "ulm_rank", "viper_rank"))
stopifnot(!anyDuplicated(cells$cell_id), all(is.finite(cells$umap_1)), all(is.finite(cells$umap_2)))
stopifnot(all(edges_all$evidence_type == "curated_prior"))
diff <- diff[tolower(diff$method) == "ulm", , drop = FALSE]
pb <- pb[tolower(pb$method) == "ulm", , drop = FALSE]
if (!nrow(diff) || !nrow(pb)) stop("Actual ULM scores and donor results are required")
ranked <- diff[order(diff$fdr, -abs(diff$effect), diff$tf, na.last = TRUE), ]
candidate_tfs <- unique(ranked$tf)
available_tfs <- sub("_activity$", "", names(cells)[grepl("_activity$", names(cells))])
umap_tfs <- head(candidate_tfs[candidate_tfs %in% available_tfs & paste0(candidate_tfs, "_expression") %in% names(cells)], cfg$selection$umap_tf_count)
if (!length(umap_tfs)) stop("No actual expression/activity TF pair in cells.csv.gz")
stopifnot(all(vapply(c(paste0(umap_tfs, "_activity"), paste0(umap_tfs, "_expression")), function(n) all(is.finite(cells[[n]])), logical(1))))
palette <- c("#4477AA", "#DD9955", "#66AABB", "#AA77AA", "#889944", "#CC6677", "#999999", "#332288", "#AA4499", "#117733", "#88CCEE", "#882255", "#661100", "#6699CC", "#888888", "#CCBB44")
cell_levels <- sort(unique(cells$cell_type))
if (length(cell_levels) > length(palette)) stop("Too many cell types for reviewed categorical palette")
cell_palette <- setNames(palette[seq_along(cell_levels)], cell_levels)
theme_set(theme_classic(base_size = 8, base_family = "Arial") + theme(
  plot.title = element_text(size = 9, face = "bold"), plot.subtitle = element_text(size = 7),
  legend.title = element_text(size = 7), legend.text = element_text(size = 6.5),
  axis.text = element_text(size = 6.5), axis.title = element_text(size = 7.5),
  strip.text = element_text(size = 7, face = "bold"), plot.tag = element_text(size = 9, face = "bold"),
  plot.caption = element_text(size = 6.5, hjust = 0), plot.margin = margin(5, 5, 5, 5),
  axis.line = element_line(linewidth = .3), axis.ticks = element_line(linewidth = .3)))
provenance <- list(backend = "R", seed = analysis$seed, style = cfg$style, data_rows = list(cells = nrow(cells), pseudobulk = nrow(pb), differential = nrow(diff), network_input = nrow(edges_all)),
  umap_sampling = "None", umap_tfs = umap_tfs, figure_inputs = cfg$figures,
  interpretation_boundaries = cfg$interpretation_boundaries, packages = setNames(lapply(needed, function(p) as.character(packageVersion(p))), needed), figures = list())
save_pub_r <- function(p, stem, height_mm, selection = NULL) {
  base <- file.path(outdir, stem)
  w <- cfg$style$width_mm / 25.4; h <- height_mm / 25.4
  svglite::svglite(paste0(base, ".svg"), width = w, height = h, bg = "white")
  print(p); grDevices::dev.off()
  grDevices::cairo_pdf(paste0(base, ".pdf"), width = w, height = h, family = "Arial", bg = "white")
  print(p); grDevices::dev.off()
  ragg::agg_png(paste0(base, ".png"), width = w, height = h, units = "in", res = 600, background = "white")
  print(p); grDevices::dev.off()
  provenance$figures[[stem]] <<- list(width_mm = cfg$style$width_mm, height_mm = height_mm, dpi = 600, selection = selection)
}
embed <- function(variable, title, mode = "activity", legend = TRUE) {
  p <- ggplot(cells, aes(umap_1, umap_2, colour = .data[[variable]])) +
    ggrastr::rasterise(geom_point(size = .16, alpha = .8), dpi = 600) +
    coord_equal() + labs(title = title, x = "Author UMAP 1", y = "Author UMAP 2", colour = NULL) +
    theme(legend.position = if (legend) "right" else "none")
  if (mode == "cell_type") p <- p + scale_colour_manual(values = cell_palette)
  else if (mode == "expression") p <- p + scale_colour_gradient(low = "#EFF3F7", high = "#336699")
  else p <- p + scale_colour_gradient2(low = "#CC6677", mid = "#F7F7F7", high = "#4477AA", midpoint = 0) +
    guides(colour = guide_colourbar(barheight = grid::unit(18, "mm"), barwidth = grid::unit(3, "mm")))
  p
}
cellplot <- embed("cell_type", "Annotated cell types", "cell_type")
tfplots <- lapply(umap_tfs, function(tf) embed(paste0(tf, "_expression"), paste(tf, "expression"), "expression") + embed(paste0(tf, "_activity"), paste(tf, "ULM activity")))
p02 <- cellplot / wrap_plots(tfplots, ncol = 1) + plot_layout(heights = c(1, length(tfplots)))
save_pub_r(p02, "Fig02_tf_activity_umap", cfg$figures$Fig02$height_mm, list(tfs = umap_tfs, cells_retained = nrow(cells), embedding = "Unchanged author X_umap"))
top_per_type <- function(n) do.call(rbind, lapply(split(ranked, ranked$cell_type), function(z) head(z, n)))
heat_tfs <- top_per_type(cfg$selection$heatmap_tf_count_per_cell_type)
heat <- merge(pb, unique(heat_tfs[c("cell_type", "tf")]), by = c("cell_type", "tf"))
zscore <- function(x) if (isTRUE(sd(x) > 0)) as.numeric(scale(x)) else rep(0, length(x))
heat$display_z <- ave(heat$score, interaction(heat$cell_type, heat$tf, drop = TRUE), FUN = zscore)
heat$tf <- factor(heat$tf, levels = rev(unique(heat_tfs$tf)))
heat$donor <- factor(heat$donor, levels = sort(unique(heat$donor)))
heatplot <- function(z, fill_label = "Within-factor z") ggplot(z, aes(donor, tf, fill = display_z)) + geom_tile() +
  facet_grid(cell_type ~ condition, scales = "free", space = "free_x") +
  scale_fill_gradient2(low = "#CC6677", mid = "#F7F7F7", high = "#4477AA", midpoint = 0, name = fill_label) +
  labs(title = "Donor regulon activity", x = "Biological donor", y = NULL) +
  theme(axis.text.x = element_text(angle = 90, vjust = .5, hjust = 1), axis.ticks = element_blank(), axis.line = element_blank())
p03 <- heatplot(heat)
save_pub_r(p03, "Fig03_donor_activity_heatmap", cfg$figures$Fig03$height_mm, list(rows_displayed = nrow(heat), tfs = unique(as.character(heat$tf)), transform = cfg$selection$heatmap_transform))
forest_data <- top_per_type(cfg$selection$forest_tf_count_per_cell_type)
forest_data$label <- paste0(forest_data$tf, ifelse(is.finite(forest_data$fdr) & forest_data$fdr < .05, " *", ""))
forest <- function(z, ncol = 3) ggplot(z, aes(effect, reorder(label, effect), colour = effect > 0)) +
  geom_vline(xintercept = 0, linewidth = .3, colour = "#999999", linetype = 2) +
  geom_errorbar(aes(xmin = ci_low, xmax = ci_high), width = .2, orientation = "y", linewidth = .45) + geom_point(size = 1.6) +
  facet_wrap(~cell_type, scales = "free_y", ncol = ncol) +
  scale_colour_manual(values = c("FALSE" = "#CC6677", "TRUE" = "#4477AA"), guide = "none") +
  labs(title = "Differential regulatory-factor activity", subtitle = "Assay-adjusted coefficient; HC3 95% CI\nExploratory; * BH q < 0.05", x = "Disease coefficient (ULM score units)", y = NULL)
p05 <- forest(forest_data)
save_pub_r(p05, "Fig05_differential_tf_activity", cfg$figures$Fig05$height_mm, list(rows_displayed = nrow(forest_data), ranking = cfg$selection$candidate_order, statistic = "Assay-adjusted disease coefficient; HC3 95% CI; BH FDR"))
network_tfs <- head(candidate_tfs[candidate_tfs %in% edges_all$source], cfg$selection$network_tf_count)
if (!length(network_tfs)) network_tfs <- head(unique(edges_all$source), cfg$selection$network_tf_count)
edge_pool <- edges_all[edges_all$source %in% network_tfs, ]
target_order <- unique(edge_pool$target[order(-abs(edge_pool$target_logcpm_change), edge_pool$target)])
targets <- head(target_order, cfg$selection$network_max_targets)
edges <- edge_pool[edge_pool$target %in% targets, ]
edges$edge_label <- ifelse(edges$weight > 0, "Activation prior", ifelse(edges$weight < 0, "Repression prior", "Unknown sign"))
network_plot <- function(display_targets = targets, prior_legend = TRUE) {
  display_edges <- edges[edges$target %in% display_targets, ]
  display_edges$y <- match(display_edges$source, network_tfs) * (length(display_targets) + 1) / (length(network_tfs) + 1)
  display_edges$yend <- match(display_edges$target, rev(display_targets))
  tnodes <- data.frame(target = rev(display_targets), y = seq_along(display_targets))
  tnodes$change <- edge_pool$target_logcpm_change[match(tnodes$target, edge_pool$target)]
  snodes <- data.frame(source = network_tfs, y = seq_along(network_tfs) * (length(display_targets) + 1) / (length(network_tfs) + 1))
  p <- ggplot() + geom_segment(data = display_edges, aes(x = .08, xend = .95, y = y, yend = yend, colour = edge_label, linetype = edge_label), linewidth = .35, alpha = .65, arrow = grid::arrow(length = grid::unit(1.4, "mm"), type = "open")) +
  geom_point(data = tnodes, aes(1, y, fill = change), shape = 21, size = 2.5, stroke = .3) +
  geom_point(data = snodes, aes(0, y), shape = 22, size = 3, fill = "#D9E5EE") +
  geom_text(data = tnodes, aes(1.05, y, label = target), hjust = 0, size = 2.5, family = "Arial") +
  geom_text(data = snodes, aes(-.08, y, label = source), hjust = 1, size = 2.6, family = "Arial", fontface = "bold") +
  scale_colour_manual(values = c("Activation prior" = "#4477AA", "Repression prior" = "#DD9955", "Unknown sign" = "#999999"), name = NULL) +
  scale_linetype_manual(values = c("Activation prior" = 1, "Repression prior" = 2, "Unknown sign" = 3), name = NULL) +
  scale_fill_gradient2(low = "#CC6677", mid = "#F7F7F7", high = "#4477AA", midpoint = 0, name = "Target logCPM change") +
  coord_cartesian(xlim = c(-.45, 1.72), ylim = c(0, length(display_targets) + 1), clip = "off") +
  labs(title = "Curated TF-target prior", subtitle = "Signed CollecTRI prior edges\nTargets coloured by expression change") + theme_void(base_family = "Arial", base_size = 8) +
  guides(fill = guide_colourbar(title.position = "top", barwidth = grid::unit(24, "mm"), barheight = grid::unit(3, "mm"), order = 1),
    colour = guide_legend(ncol = 1, order = 2), linetype = guide_legend(ncol = 1, order = 2)) +
  theme(plot.title = element_text(size = 9, face = "bold"), plot.subtitle = element_text(size = 7), legend.position = "bottom", legend.box = "vertical", legend.box.just = "left", legend.title = element_text(size = 6.5), legend.text = element_text(size = 6.5), legend.spacing.y = grid::unit(1, "mm"), plot.margin = margin(5, 5, 5, 5))
  if (!prior_legend) p <- p + guides(colour = "none", linetype = "none") + labs(subtitle = "Blue solid: activation; orange dashed: repression\nSigned prior targets; expression-coloured nodes")
  p
}
p04 <- network_plot()
save_pub_r(p04, "Fig04_curated_tf_target_network", cfg$figures$Fig04$height_mm, list(input_edges = nrow(edges_all), displayed_edges = nrow(edges), tfs = network_tfs, targets = targets, selection_rule = cfg$selection$network_selection, evidence_type = "curated_prior"))
profile <- profile[profile$tf %in% head(candidate_tfs, 12), ]
profile$display_z <- ave(profile$mean_activity, profile$tf, FUN = zscore)
p09 <- ggplot(profile, aes(cell_type, tf, colour = display_z, size = n_cells)) + geom_point() + facet_wrap(~condition) +
  scale_colour_gradient2(low = "#CC6677", mid = "#F7F7F7", high = "#4477AA", midpoint = 0, name = "Within-factor z") +
  scale_size_area(max_size = 4, name = "Cells") + labs(title = "Cell-type regulatory activity profile", subtitle = "Descriptive mean ULM activity; RSS not computed", x = NULL, y = NULL) +
  theme(axis.text.x = element_text(angle = 30, hjust = 1))
save_pub_r(p09, "Fig09_celltype_activity_profile", cfg$figures$Fig09$height_mm, list(rows_displayed = nrow(profile), statistic = "Descriptive cell mean ULM activity; not RSS", transform = cfg$selection$dotplot_transform))
concordance <- function(z) {
  stats <- do.call(rbind, lapply(split(z, z$cell_type), function(x) data.frame(cell_type = x$cell_type[1], label = sprintf("Spearman rho = %.2f\nn = %s regulators", cor(x$ulm_rank, x$viper_rank, method = "spearman"), nrow(x)))))
  z$facet_label <- paste(z$cell_type, stats$label[match(z$cell_type, stats$cell_type)], sep = " | ")
  labels <- z[z$tf %in% head(candidate_tfs, 3), ]
  ggplot(z, aes(ulm_rank, viper_rank)) + geom_abline(slope = 1, intercept = 0, colour = "#CCCCCC", linewidth = .3) + geom_point(size = 1.2, colour = "#4477AA", alpha = .7) +
    geom_point(data = labels, aes(shape = tf), size = 2, colour = "#CC6677") +
    facet_wrap(~facet_label) + labs(title = "Method rank concordance", subtitle = "Nominal disease-association P-value ranks\nULM vs original VIPER; shared CollecTRI", x = "ULM association rank", y = "VIPER association rank", shape = NULL) + theme(legend.position = "bottom")
}
p12 <- concordance(conc)
save_pub_r(p12, "Fig12_method_concordance", cfg$figures$Fig12$height_mm, list(rows_displayed = nrow(conc), statistic = "Descriptive Spearman correlation of nominal disease-association P-value ranks across shared TFs; not independent validation", implementation = "Original Bioconductor VIPER 1.36.0", labelled_tfs = head(candidate_tfs, 3)))
steps <- data.frame(x = rep(c(1, 3, 5), 2), y = rep(c(3, 1), each = 3),
  label = c(sprintf("Public periodontal atlas\n%s analyzed cells\nRaw counts + author UMAP", format(nrow(cells), big.mark = ",")),
  "Source and donor audit\nWithin-study condition mapping\nAssay/platform sensitivity", "Signed CollecTRI prior\nHuman gene symbols\nObserved-target coverage", "Candidate prioritization\nPrior targets + regulators\nProposed experimental validation", "Donor-level inference\nAssay-adjusted model + HC3 CI\nFDR + stability checks", "Matched activity scoring\nULM + VIPER scoring\nDonor x cell-type pseudobulk"))
p01 <- ggplot(steps, aes(x, y)) + geom_rect(aes(xmin = x - .83, xmax = x + .83, ymin = y - .55, ymax = y + .55), fill = "#EEF3F7", colour = "#91A8BC", linewidth = .45) +
  geom_text(aes(label = label), size = 2.7, family = "Arial", lineheight = 1.25) +
  annotate("segment", x = c(1.87, 3.87, 5, 4.13, 2.13), xend = c(2.1, 4.1, 5, 3.9, 1.9), y = c(3, 3, 2.42, 1, 1), yend = c(3, 3, 1.58, 1, 1), linewidth = .5, colour = "#4477AA", arrow = grid::arrow(length = grid::unit(2, "mm"))) +
  coord_cartesian(xlim = c(0, 6), ylim = c(.1, 3.9)) + theme_void(base_family = "Arial", base_size = 8) +
  labs(title = "Executed regulatory-activity workflow", subtitle = "Cells describe local patterns; donors support exploratory disease inference") + theme(plot.title = element_text(size = 10, face = "bold"), plot.subtitle = element_text(size = 8))
save_pub_r(p01, "Fig01_analysis_workflow", cfg$figures$Fig01$height_mm)
focus_type <- if ("contrast_cell_type" %in% names(edges_all)) as.character(edges_all$contrast_cell_type[1]) else as.character(ranked$cell_type[1])
metadata <- read_result("pseudobulk_metadata.csv", c("sample", "donor", "condition", "cell_type"))
pathway_matrix <- read.csv(file.path(tabdir, "progeny_activity_matrix.csv"), row.names = 1, check.names = FALSE)
pathway_long <- data.frame(sample = rep(rownames(pathway_matrix), times = ncol(pathway_matrix)), tf = rep(colnames(pathway_matrix), each = nrow(pathway_matrix)), score = as.vector(as.matrix(pathway_matrix)))
pathway_long <- merge(pathway_long, metadata, by = "sample")
pathway_long$display_z <- ave(pathway_long$score, interaction(pathway_long$cell_type, pathway_long$tf, drop = TRUE), FUN = zscore)
pathway_differential <- read_result("progeny_differential.csv", c("cell_type", "pathway", "effect", "ci_low", "ci_high", "fdr"))
pathway_differential$label <- paste0(pathway_differential$pathway, ifelse(pathway_differential$fdr < .05, " *", ""))
pathway_forest <- function(z) ggplot(z, aes(effect, reorder(label, effect))) +
  geom_vline(xintercept = 0, colour = "#999999", linetype = 2, linewidth = .3) +
  geom_errorbar(aes(xmin = ci_low, xmax = ci_high), orientation = "y", width = .2, colour = "#4477AA", linewidth = .4) + geom_point(size = 1.4, colour = "#4477AA") +
  facet_wrap(~cell_type, scales = "free_y") + labs(title = "Pathway footprint activity", subtitle = "PROGENy ULM; assay-adjusted donor model\nHC3 95% CI; * BH q < 0.05", x = "Disease coefficient", y = NULL)
p13 <- heatplot(pathway_long, "Within-pathway z") + labs(title = "Donor pathway activity", subtitle = "PROGENy footprints; within-pathway z-score")
save_pub_r(p13, "Fig13_progeny_donor_pathways", 165, list(rows_displayed = nrow(pathway_long), statistic = "PROGENy pathway activity, not TF activity"))
save_pub_r(pathway_forest(pathway_differential), "Fig13b_progeny_disease_effects", 125, list(rows_displayed = nrow(pathway_differential), statistic = "Assay-adjusted donor pathway coefficient; HC3 95% CI; BH FDR"))
vipermatrix <- read.csv(file.path(tabdir, "bioc_viper_activity_matrix.csv"), row.names = 1, check.names = FALSE)
vheat <- data.frame(sample = rep(rownames(vipermatrix), times = ncol(vipermatrix)), tf = rep(colnames(vipermatrix), each = nrow(vipermatrix)), score = as.vector(as.matrix(vipermatrix)))
vheat <- merge(merge(vheat, metadata, by = "sample"), unique(heat_tfs[c("cell_type", "tf")]), by = c("cell_type", "tf"))
vheat$display_z <- ave(vheat$score, interaction(vheat$cell_type, vheat$tf, drop = TRUE), FUN = zscore)
vheat$tf <- factor(vheat$tf, levels = levels(heat$tf))
p14 <- heatplot(vheat) + labs(title = "Original VIPER donor activity", subtitle = "Bioconductor VIPER 1.36.0; same CollecTRI prior; within-factor z-score")
save_pub_r(p14, "Fig14_original_viper_activity", 155, list(rows_displayed = nrow(vheat), implementation = "Original Bioconductor VIPER 1.36.0", targets = "Same filtered CollecTRI prior"))
links <- read_result("tf_pathway_links.csv", c("tf", "pathway", "overlap", "fdr", "evidence_type"))
stopifnot(all(links$evidence_type == "curated_prior_gene_set_overlap"), all(is.finite(links$fdr)), all(links$fdr >= 0))
pathway_rank <- aggregate(fdr ~ pathway, links, min)
shown_sets <- head(pathway_rank$pathway[order(pathway_rank$fdr, pathway_rank$pathway)], 6)
shown_links <- links[links$pathway %in% shown_sets, ]
shown_links$display_logq <- -log10(pmax(shown_links$fdr, .Machine$double.xmin))
shown_links$pathway <- factor(shown_links$pathway, levels = rev(shown_sets))
wrap_label <- function(x) vapply(x, function(y) paste(strwrap(y, width = 24), collapse = "\n"), character(1))
p15 <- ggplot(shown_links, aes(tf, pathway, size = overlap, colour = display_logq)) + geom_point() +
  scale_size_area(max_size = 4, name = "Shared targets") + scale_colour_gradient(low = "#D9E5EE", high = "#336699", name = "-log10(BH q)") +
  scale_y_discrete(labels = wrap_label) + labs(title = "Prior-target gene-set overlap", subtitle = "CollecTRI targets and Hallmark gene sets\nPrior overlap; not measured pathway activation", x = NULL, y = NULL) +
  guides(size = guide_legend(nrow = 1, order = 2), colour = guide_colourbar(title.position = "top", barwidth = grid::unit(22, "mm"), barheight = grid::unit(3, "mm"), order = 1)) +
  theme(axis.text.x = element_text(angle = 50, hjust = 1), legend.position = "bottom", legend.box = "vertical", legend.title = element_text(size = 6.5))
save_pub_r(p15, "Fig15_tf_hallmark_overlap", 110, list(input_rows = nrow(links), displayed_rows = nrow(shown_links), gene_sets = shown_sets, selection = "Six gene sets with lowest observed minimum BH q; all supplied TF pairs retained for these sets", statistic = "Curated-prior target overlap; not coexpression modules or disease pathway activation"))
paired <- read_result("donor_expression_activity.csv", c("donor", "condition", "cell_type", "tf", "expression_logcpm", "activity"))
paired <- paired[paired$tf %in% umap_tfs, ]
p16 <- ggplot(paired, aes(expression_logcpm, activity, colour = condition, shape = condition)) + geom_point(size = 1.8, alpha = .85) +
  facet_grid(cell_type ~ tf, scales = "free") + scale_colour_manual(values = c("Healthy" = "#4477AA", "Periodontitis" = "#DD9955")) +
  labs(title = "Regulator expression and inferred activity", subtitle = "Matched donor pseudobulk observations; descriptive comparison", x = "Regulator expression (logCPM)", y = "ULM activity", colour = NULL, shape = NULL) + theme(legend.position = "bottom")
save_pub_r(p16, "Fig16_donor_expression_activity", 135, list(rows_displayed = nrow(paired), tfs = umap_tfs, unit = "Matched biological donor x cell type", statistic = "Raw paired expression/activity observations; no fitted causal relationship"))
compact_targets <- head(targets, 10)
compact_network <- network_plot(compact_targets, FALSE)
compact_forest <- forest_data[forest_data$cell_type == focus_type, ]
compact_forest <- head(compact_forest[order(compact_forest$fdr, -abs(compact_forest$effect)), ], 8)
compact_heat <- heat[heat$cell_type == focus_type & heat$tf %in% compact_forest$tf, ]
compact_links <- shown_links[shown_links$pathway %in% head(shown_sets, 3), ]
compact_overlap <- p15 %+% compact_links + guides(size = "none") +
  labs(subtitle = "Prior overlap; size = shared targets\nColour = -log10(BH q)")
pathway_focus <- pathway_differential[pathway_differential$cell_type == focus_type, ]
pathway_focus <- head(pathway_focus[order(pathway_focus$fdr, -abs(pathway_focus$effect)), ], 5)
composite <- (cellplot | embed(paste0(umap_tfs[1], "_activity"), paste(umap_tfs[1], "inferred activity"))) /
  (forest(compact_forest, 1) | heatplot(compact_heat)) /
  (compact_network | concordance(conc[conc$cell_type == focus_type, ])) /
  (pathway_forest(pathway_focus) | compact_overlap) +
  plot_layout(heights = c(1, 1.2, 1.3, .95)) + plot_annotation(title = "Transcriptional regulatory landscape of periodontal inflammation", subtitle = paste("Exploratory donor-based comparison | Donor and prior-network focus:", focus_type), tag_levels = "a", theme = theme(plot.title = element_text(size = 10, face = "bold"), plot.subtitle = element_text(size = 7.5)))
save_pub_r(composite, "Composite_periodontal_regulatory_landscape", cfg$figures$Composite$height_mm, list(focus_cell_type = focus_type, focus_tf = umap_tfs[1], panels = c("cell embedding", "TF activity", "donor disease coefficients", "donor regulon heatmap", "curated prior network", "algorithm concordance", "PROGENy pathway effects", "prior-target Hallmark overlap"), pathway_focus = as.character(pathway_focus$pathway), compact_forest_tfs = compact_forest$tf, compact_network_targets = compact_targets, compact_overlap_sets = head(shown_sets, 3)))
input_files <- list.files(tabdir, pattern = "\\.csv(\\.gz)?$", full.names = TRUE)
provenance$input_table_md5 <- as.list(setNames(unname(tools::md5sum(input_files)), basename(input_files)))
provenance$figure_inputs <- lapply(cfg$figures, function(z) z$input)
jsonlite::write_json(provenance, file.path(outdir, "figure_provenance.json"), auto_unbox = TRUE, pretty = TRUE, na = "null")
writeLines(capture.output(sessionInfo()), file.path(outdir, "R_plot_sessionInfo.txt"))
cat("Generated thirteen real-data figure bundles in ", outdir, "\n", sep = "")
