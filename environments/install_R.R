# Use an isolated library. For the exact executed stack use R 4.3.x + Bioc 3.18.
lib <- Sys.getenv("R_LIBS_USER", unset = "data/local/Rlibrary")
dir.create(lib, recursive = TRUE, showWarnings = FALSE)
.libPaths(c(lib, .libPaths()))
options(repos = c(CRAN = "https://cloud.r-project.org"))
if (!requireNamespace("BiocManager", quietly = TRUE)) install.packages("BiocManager", lib = lib)
if (getRversion() >= "4.3" && getRversion() < "4.4") {
  BiocManager::install(version = "3.18", ask = FALSE, update = FALSE, lib = lib)
}
BiocManager::install("viper", ask = FALSE, update = FALSE, lib = lib)
install.packages(c("ggplot2", "patchwork", "jsonlite", "svglite", "ragg", "ggrepel", "ggrastr", "dplyr", "tidyr"), lib = lib)
cat("Installed package versions must be compared with R_runtime.json and R_plot_sessionInfo.txt.\n")
