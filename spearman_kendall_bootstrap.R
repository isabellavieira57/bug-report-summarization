test<-("\n\n")
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

# bootstrap 341

#SimCosseno original
arquivo <- read.table("resultados/resultadosRanking/rankingSimCosseno_original_bootstrap341.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 0:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 3, 21, 29, 31, 35, 5, 6, 9, 7, 8, 12, 13, 15, 17, 19, 22, 23, 24, 25, 26, 28, 30, 32, 33, 34, 40, 36, 2, 4, 10, 11, 16, 18, 20, 37, 38, 14, 27, 39)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 341		", kendall,"		", spearman, "				(1) SIM COSSENO: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#SimCosseno transformada
arquivo <- read.table("resultados/resultadosRanking/rankingSimCosseno_transformada_bootstrap341.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 3, 21, 29, 31, 35, 5, 6, 9, 7, 8, 12, 13, 15, 17, 19, 22, 23, 24, 25, 26, 28, 30, 32, 33, 34, 40, 36, 2, 4, 10, 11, 16, 18, 20, 37, 38, 14, 27, 39)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 341		", kendall,"		", spearman, "				(1) SIM COSSENO: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Euclidiana original
arquivo <- read.table("resultados/resultadosRanking/rankingEuclidiana_original_bootstrap341.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 3, 21, 29, 31, 35, 5, 6, 9, 7, 8, 12, 13, 15, 17, 19, 22, 23, 24, 25, 26, 28, 30, 32, 33, 34, 40, 36, 2, 4, 10, 11, 16, 18, 20, 37, 38, 14, 27, 39)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 341		", kendall,"		", spearman, "				(1) EUCLIDIANA: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Euclidiana transformada
arquivo <- read.table("resultados/resultadosRanking/rankingEuclidiana_transformada_bootstrap341.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 3, 21, 29, 31, 35, 5, 6, 9, 7, 8, 12, 13, 15, 17, 19, 22, 23, 24, 25, 26, 28, 30, 32, 33, 34, 40, 36, 2, 4, 10, 11, 16, 18, 20, 37, 38, 14, 27, 39)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 341		", kendall,"		", spearman, "				(1) EUCLIDIANA: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#PageRank original
arquivo <- read.table("resultados/resultadosRanking/rankingPageRank_original_bootstrap341.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 3, 21, 29, 31, 35, 5, 6, 9, 7, 8, 12, 13, 15, 17, 19, 22, 23, 24, 25, 26, 28, 30, 32, 33, 34, 40, 36, 2, 4, 10, 11, 16, 18, 20, 37, 38, 14, 27, 39)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 341		", kendall,"		", spearman, "				(2) PAGERANK: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#PageRank transformada
arquivo <- read.table("resultados/resultadosRanking/rankingPageRank_transformada_bootstrap341.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 3, 21, 29, 31, 35, 5, 6, 9, 7, 8, 12, 13, 15, 17, 19, 22, 23, 24, 25, 26, 28, 30, 32, 33, 34, 40, 36, 2, 4, 10, 11, 16, 18, 20, 37, 38, 14, 27, 39)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 341		", kendall,"		", spearman, "				(2) PAGERANK: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Massey original
arquivo <- read.table("resultados/resultadosRanking/rankingMassey_original_bootstrap341.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 3, 21, 29, 31, 35, 5, 6, 9, 7, 8, 12, 13, 15, 17, 19, 22, 23, 24, 25, 26, 28, 30, 32, 33, 34, 40, 36, 2, 4, 10, 11, 16, 18, 20, 37, 38, 14, 27, 39)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 341		", kendall,"		", spearman, "				(2) MASSEY: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Massey transformada
arquivo <- read.table("resultados/resultadosRanking/rankingMassey_transformada_bootstrap341.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 3, 21, 29, 31, 35, 5, 6, 9, 7, 8, 12, 13, 15, 17, 19, 22, 23, 24, 25, 26, 28, 30, 32, 33, 34, 40, 36, 2, 4, 10, 11, 16, 18, 20, 37, 38, 14, 27, 39)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 341		", kendall,"		", spearman, "				(2) MASSEY: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Colley original
arquivo <- read.table("resultados/resultadosRanking/rankingColley_original_bootstrap341.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 3, 21, 29, 31, 35, 5, 6, 9, 7, 8, 12, 13, 15, 17, 19, 22, 23, 24, 25, 26, 28, 30, 32, 33, 34, 40, 36, 2, 4, 10, 11, 16, 18, 20, 37, 38, 14, 27, 39)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 341		", kendall,"		", spearman, "				(2) COLLEY: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Colley original
arquivo <- read.table("resultados/resultadosRanking/rankingColley_transformada_bootstrap341.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 3, 21, 29, 31, 35, 5, 6, 9, 7, 8, 12, 13, 15, 17, 19, 22, 23, 24, 25, 26, 28, 30, 32, 33, 34, 40, 36, 2, 4, 10, 11, 16, 18, 20, 37, 38, 14, 27, 39)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 341		", kendall,"		", spearman, "				(2) COLLEY: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Louvain + PageRank Original
arquivo <- read.table("resultados/resultadosRanking/rankingLouvain+PageRank_original_bootstrap341.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 3, 21, 29, 31, 35, 5, 6, 9, 7, 8, 12, 13, 15, 17, 19, 22, 23, 24, 25, 26, 28, 30, 32, 33, 34, 40, 36, 2, 4, 10, 11, 16, 18, 20, 37, 38, 14, 27, 39)
oraculo <- head(oraculo, numLinhas)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 341		", kendall,"		", spearman, "				(3) LOUVAIN + PAGERANK: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Louvain + PageRank transformada
arquivo <- read.table("resultados/resultadosRanking/rankingLouvain+PageRank_transformada_bootstrap341.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 3, 21, 29, 31, 35, 5, 6, 9, 7, 8, 12, 13, 15, 17, 19, 22, 23, 24, 25, 26, 28, 30, 32, 33, 34, 40, 36, 2, 4, 10, 11, 16, 18, 20, 37, 38, 14, 27, 39)
oraculo <- head(oraculo, numLinhas)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 341		", kendall,"		", spearman, "				(3) LOUVAIN + PAGERANK: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Louvain + Centralidade Original
arquivo <- read.table("resultados/resultadosRanking/rankingLouvain+Centralidade_original_bootstrap341.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 3, 21, 29, 31, 35, 5, 6, 9, 7, 8, 12, 13, 15, 17, 19, 22, 23, 24, 25, 26, 28, 30, 32, 33, 34, 40, 36, 2, 4, 10, 11, 16, 18, 20, 37, 38, 14, 27, 39)
oraculo <- head(oraculo, numLinhas)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 341		", kendall,"		", spearman, "				(3) LOUVAIN + CENTRALIDADE: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Louvain + Centralidade transformada
arquivo <- read.table("resultados/resultadosRanking/rankingLouvain+Centralidade_transformada_bootstrap341.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 3, 21, 29, 31, 35, 5, 6, 9, 7, 8, 12, 13, 15, 17, 19, 22, 23, 24, 25, 26, 28, 30, 32, 33, 34, 40, 36, 2, 4, 10, 11, 16, 18, 20, 37, 38, 14, 27, 39)
oraculo <- head(oraculo, numLinhas)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 341		", kendall,"		", spearman, "				(3) LOUVAIN + CENTRALIDADE: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

test<-("\n\n")
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#----------------------------------------------------------------------------------------#
#bootstrap 1235

#SimCosseno original
arquivo <- read.table("resultados/resultadosRanking/rankingSimCosseno_original_bootstrap1235.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 0:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 2, 5, 11, 18, 19, 30, 3, 7, 8, 10, 14, 15, 20, 22, 24, 25, 26, 29, 21, 31, 9, 12, 32, 33, 4, 6, 13, 16, 17, 23, 27, 28)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 1235		", kendall,"		", spearman, "				(1) SIM COSSENO: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#SimCosseno transformada
arquivo <- read.table("resultados/resultadosRanking/rankingSimCosseno_transformada_bootstrap1235.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 2, 5, 11, 18, 19, 30, 3, 7, 8, 10, 14, 15, 20, 22, 24, 25, 26, 29, 21, 31, 9, 12, 32, 33, 4, 6, 13, 16, 17, 23, 27, 28)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 1235		", kendall,"		", spearman, "				(1) SIM COSSENO: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Euclidiana original
arquivo <- read.table("resultados/resultadosRanking/rankingEuclidiana_original_bootstrap1235.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 2, 5, 11, 18, 19, 30, 3, 7, 8, 10, 14, 15, 20, 22, 24, 25, 26, 29, 21, 31, 9, 12, 32, 33, 4, 6, 13, 16, 17, 23, 27, 28)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 1235		", kendall,"		", spearman, "				(1) EUCLIDIANA: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Euclidiana transformada
arquivo <- read.table("resultados/resultadosRanking/rankingEuclidiana_transformada_bootstrap1235.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 2, 5, 11, 18, 19, 30, 3, 7, 8, 10, 14, 15, 20, 22, 24, 25, 26, 29, 21, 31, 9, 12, 32, 33, 4, 6, 13, 16, 17, 23, 27, 28)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 1235		", kendall,"		", spearman, "				(1) EUCLIDIANA: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#PageRank original
arquivo <- read.table("resultados/resultadosRanking/rankingPageRank_original_bootstrap1235.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 2, 5, 11, 18, 19, 30, 3, 7, 8, 10, 14, 15, 20, 22, 24, 25, 26, 29, 21, 31, 9, 12, 32, 33, 4, 6, 13, 16, 17, 23, 27, 28)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 1235		", kendall,"		", spearman, "				(2) PAGERANK: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#PageRank transformada
arquivo <- read.table("resultados/resultadosRanking/rankingPageRank_transformada_bootstrap1235.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 2, 5, 11, 18, 19, 30, 3, 7, 8, 10, 14, 15, 20, 22, 24, 25, 26, 29, 21, 31, 9, 12, 32, 33, 4, 6, 13, 16, 17, 23, 27, 28)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 1235		", kendall,"		", spearman, "				(2) PAGERANK: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Massey original
arquivo <- read.table("resultados/resultadosRanking/rankingMassey_original_bootstrap1235.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 2, 5, 11, 18, 19, 30, 3, 7, 8, 10, 14, 15, 20, 22, 24, 25, 26, 29, 21, 31, 9, 12, 32, 33, 4, 6, 13, 16, 17, 23, 27, 28)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 1235		", kendall,"		", spearman, "				(2) MASSEY: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Massey transformada
arquivo <- read.table("resultados/resultadosRanking/rankingMassey_transformada_bootstrap1235.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 2, 5, 11, 18, 19, 30, 3, 7, 8, 10, 14, 15, 20, 22, 24, 25, 26, 29, 21, 31, 9, 12, 32, 33, 4, 6, 13, 16, 17, 23, 27, 28)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 1235		", kendall,"		", spearman, "				(2) MASSEY: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Colley original
arquivo <- read.table("resultados/resultadosRanking/rankingColley_original_bootstrap1235.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 2, 5, 11, 18, 19, 30, 3, 7, 8, 10, 14, 15, 20, 22, 24, 25, 26, 29, 21, 31, 9, 12, 32, 33, 4, 6, 13, 16, 17, 23, 27, 28)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 1235		", kendall,"		", spearman, "				(2) COLLEY: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Colley original
arquivo <- read.table("resultados/resultadosRanking/rankingColley_transformada_bootstrap1235.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 2, 5, 11, 18, 19, 30, 3, 7, 8, 10, 14, 15, 20, 22, 24, 25, 26, 29, 21, 31, 9, 12, 32, 33, 4, 6, 13, 16, 17, 23, 27, 28)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 1235		", kendall,"		", spearman, "				(2) COLLEY: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Louvain + PageRank Original
arquivo <- read.table("resultados/resultadosRanking/rankingLouvain+PageRank_original_bootstrap1235.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 2, 5, 11, 18, 19, 30, 3, 7, 8, 10, 14, 15, 20, 22, 24, 25, 26, 29, 21, 31, 9, 12, 32, 33, 4, 6, 13, 16, 17, 23, 27, 28)
oraculo <- head(oraculo, numLinhas)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 1235		", kendall,"		", spearman, "				(3) LOUVAIN + PAGERANK: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Louvain + PageRank transformada
arquivo <- read.table("resultados/resultadosRanking/rankingLouvain+PageRank_transformada_bootstrap1235.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 2, 5, 11, 18, 19, 30, 3, 7, 8, 10, 14, 15, 20, 22, 24, 25, 26, 29, 21, 31, 9, 12, 32, 33, 4, 6, 13, 16, 17, 23, 27, 28)
oraculo <- head(oraculo, numLinhas)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 1235		", kendall,"		", spearman, "				(3) LOUVAIN + PAGERANK: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Louvain + Centralidade Original
arquivo <- read.table("resultados/resultadosRanking/rankingLouvain+Centralidade_original_bootstrap1235.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 2, 5, 11, 18, 19, 30, 3, 7, 8, 10, 14, 15, 20, 22, 24, 25, 26, 29, 21, 31, 9, 12, 32, 33, 4, 6, 13, 16, 17, 23, 27, 28)
oraculo <- head(oraculo, numLinhas)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 1235		", kendall,"		", spearman, "				(3) LOUVAIN + CENTRALIDADE: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Louvain + Centralidade transformada
arquivo <- read.table("resultados/resultadosRanking/rankingLouvain+Centralidade_transformada_bootstrap1235.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 2, 5, 11, 18, 19, 30, 3, 7, 8, 10, 14, 15, 20, 22, 24, 25, 26, 29, 21, 31, 9, 12, 32, 33, 4, 6, 13, 16, 17, 23, 27, 28)
oraculo <- head(oraculo, numLinhas)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 1235		", kendall,"		", spearman, "				(3) LOUVAIN + CENTRALIDADE: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

test<-("\n\n")
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#----------------------------------------------------------------------------------------#
#bootstrap 931

#SimCosseno original
arquivo <- read.table("resultados/resultadosRanking/rankingSimCosseno_original_bootstrap931.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 0:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 9, 13, 14, 17, 21, 24, 25, 26, 28, 34, 2, 5, 10, 11, 12, 16, 18, 19, 22, 23, 29, 30, 32, 33, 35, 3, 4, 6, 7, 8, 15, 27, 31, 20)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 931		", kendall,"		", spearman, "				(1) SIM COSSENO: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#SimCosseno transformada
arquivo <- read.table("resultados/resultadosRanking/rankingSimCosseno_transformada_bootstrap931.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 9, 13, 14, 17, 21, 24, 25, 26, 28, 34, 2, 5, 10, 11, 12, 16, 18, 19, 22, 23, 29, 30, 32, 33, 35, 3, 4, 6, 7, 8, 15, 27, 31, 20)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 931		", kendall,"		", spearman, "				(1) SIM COSSENO: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Euclidiana original
arquivo <- read.table("resultados/resultadosRanking/rankingEuclidiana_original_bootstrap931.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 9, 13, 14, 17, 21, 24, 25, 26, 28, 34, 2, 5, 10, 11, 12, 16, 18, 19, 22, 23, 29, 30, 32, 33, 35, 3, 4, 6, 7, 8, 15, 27, 31, 20)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 931		", kendall,"		", spearman, "				(1) EUCLIDIANA: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Euclidiana transformada
arquivo <- read.table("resultados/resultadosRanking/rankingEuclidiana_transformada_bootstrap931.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 9, 13, 14, 17, 21, 24, 25, 26, 28, 34, 2, 5, 10, 11, 12, 16, 18, 19, 22, 23, 29, 30, 32, 33, 35, 3, 4, 6, 7, 8, 15, 27, 31, 20)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 931		", kendall,"		", spearman, "				(1) EUCLIDIANA: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#PageRank original
arquivo <- read.table("resultados/resultadosRanking/rankingPageRank_original_bootstrap931.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 9, 13, 14, 17, 21, 24, 25, 26, 28, 34, 2, 5, 10, 11, 12, 16, 18, 19, 22, 23, 29, 30, 32, 33, 35, 3, 4, 6, 7, 8, 15, 27, 31, 20)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 931		", kendall,"		", spearman, "				(2) PAGERANK: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#PageRank transformada
arquivo <- read.table("resultados/resultadosRanking/rankingPageRank_transformada_bootstrap931.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 9, 13, 14, 17, 21, 24, 25, 26, 28, 34, 2, 5, 10, 11, 12, 16, 18, 19, 22, 23, 29, 30, 32, 33, 35, 3, 4, 6, 7, 8, 15, 27, 31, 20)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 931		", kendall,"		", spearman, "				(2) PAGERANK: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Massey original
arquivo <- read.table("resultados/resultadosRanking/rankingMassey_original_bootstrap931.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 9, 13, 14, 17, 21, 24, 25, 26, 28, 34, 2, 5, 10, 11, 12, 16, 18, 19, 22, 23, 29, 30, 32, 33, 35, 3, 4, 6, 7, 8, 15, 27, 31, 20)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 931		", kendall,"		", spearman, "				(2) MASSEY: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Massey transformada
arquivo <- read.table("resultados/resultadosRanking/rankingMassey_transformada_bootstrap931.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 9, 13, 14, 17, 21, 24, 25, 26, 28, 34, 2, 5, 10, 11, 12, 16, 18, 19, 22, 23, 29, 30, 32, 33, 35, 3, 4, 6, 7, 8, 15, 27, 31, 20)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 931		", kendall,"		", spearman, "				(2) MASSEY: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Colley original
arquivo <- read.table("resultados/resultadosRanking/rankingColley_original_bootstrap931.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 9, 13, 14, 17, 21, 24, 25, 26, 28, 34, 2, 5, 10, 11, 12, 16, 18, 19, 22, 23, 29, 30, 32, 33, 35, 3, 4, 6, 7, 8, 15, 27, 31, 20)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 931		", kendall,"		", spearman, "				(2) COLLEY: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Colley original
arquivo <- read.table("resultados/resultadosRanking/rankingColley_transformada_bootstrap931.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 9, 13, 14, 17, 21, 24, 25, 26, 28, 34, 2, 5, 10, 11, 12, 16, 18, 19, 22, 23, 29, 30, 32, 33, 35, 3, 4, 6, 7, 8, 15, 27, 31, 20)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 931		", kendall,"		", spearman, "				(2) COLLEY: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Louvain + PageRank Original
arquivo <- read.table("resultados/resultadosRanking/rankingLouvain+PageRank_original_bootstrap931.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 9, 13, 14, 17, 21, 24, 25, 26, 28, 34, 2, 5, 10, 11, 12, 16, 18, 19, 22, 23, 29, 30, 32, 33, 35, 3, 4, 6, 7, 8, 15, 27, 31, 20)
oraculo <- head(oraculo, numLinhas)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 931		", kendall,"		", spearman, "				(3) LOUVAIN + PAGERANK: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Louvain + PageRank transformada
arquivo <- read.table("resultados/resultadosRanking/rankingLouvain+PageRank_transformada_bootstrap931.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 9, 13, 14, 17, 21, 24, 25, 26, 28, 34, 2, 5, 10, 11, 12, 16, 18, 19, 22, 23, 29, 30, 32, 33, 35, 3, 4, 6, 7, 8, 15, 27, 31, 20)
oraculo <- head(oraculo, numLinhas)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 931		", kendall,"		", spearman, "				(3) LOUVAIN + PAGERANK: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Louvain + Centralidade Original
arquivo <- read.table("resultados/resultadosRanking/rankingLouvain+Centralidade_original_bootstrap931.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 9, 13, 14, 17, 21, 24, 25, 26, 28, 34, 2, 5, 10, 11, 12, 16, 18, 19, 22, 23, 29, 30, 32, 33, 35, 3, 4, 6, 7, 8, 15, 27, 31, 20)
oraculo <- head(oraculo, numLinhas)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 931		", kendall,"		", spearman, "				(3) LOUVAIN + CENTRALIDADE: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Louvain + Centralidade transformada
arquivo <- read.table("resultados/resultadosRanking/rankingLouvain+Centralidade_transformada_bootstrap931.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 9, 13, 14, 17, 21, 24, 25, 26, 28, 34, 2, 5, 10, 11, 12, 16, 18, 19, 22, 23, 29, 30, 32, 33, 35, 3, 4, 6, 7, 8, 15, 27, 31, 20)
oraculo <- head(oraculo, numLinhas)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 931		", kendall,"		", spearman, "				(3) LOUVAIN + CENTRALIDADE: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

test<-("\n\n")
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#----------------------------------------------------------------------------------------#
#bootstrap 1602

#SimCosseno original
arquivo <- read.table("resultados/resultadosRanking/rankingSimCosseno_original_bootstrap1602.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 0:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 4, 5, 17, 20, 23, 28, 3, 6, 2, 7, 8, 9, 11, 12, 13, 14, 15, 16, 18, 19, 21, 22, 24, 25, 26, 27, 38, 39, 40, 29, 34, 10, 30,31, 32, 33, 35, 36, 37)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 1602		", kendall,"		", spearman, "				(1) SIM COSSENO: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#SimCosseno transformada
arquivo <- read.table("resultados/resultadosRanking/rankingSimCosseno_transformada_bootstrap1602.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 4, 5, 17, 20, 23, 28, 3, 6, 2, 7, 8, 9, 11, 12, 13, 14, 15, 16, 18, 19, 21, 22, 24, 25, 26, 27, 38, 39, 40, 29, 34, 10, 30,31, 32, 33, 35, 36, 37)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 1602		", kendall,"		", spearman, "				(1) SIM COSSENO: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Euclidiana original
arquivo <- read.table("resultados/resultadosRanking/rankingEuclidiana_original_bootstrap1602.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 4, 5, 17, 20, 23, 28, 3, 6, 2, 7, 8, 9, 11, 12, 13, 14, 15, 16, 18, 19, 21, 22, 24, 25, 26, 27, 38, 39, 40, 29, 34, 10, 30,31, 32, 33, 35, 36, 37)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 1602		", kendall,"		", spearman, "				(1) EUCLIDIANA: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Euclidiana transformada
arquivo <- read.table("resultados/resultadosRanking/rankingEuclidiana_transformada_bootstrap1602.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 4, 5, 17, 20, 23, 28, 3, 6, 2, 7, 8, 9, 11, 12, 13, 14, 15, 16, 18, 19, 21, 22, 24, 25, 26, 27, 38, 39, 40, 29, 34, 10, 30,31, 32, 33, 35, 36, 37)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 1602		", kendall,"		", spearman, "				(1) EUCLIDIANA: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#PageRank original
arquivo <- read.table("resultados/resultadosRanking/rankingPageRank_original_bootstrap1602.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 4, 5, 17, 20, 23, 28, 3, 6, 2, 7, 8, 9, 11, 12, 13, 14, 15, 16, 18, 19, 21, 22, 24, 25, 26, 27, 38, 39, 40, 29, 34, 10, 30,31, 32, 33, 35, 36, 37)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 1602		", kendall,"		", spearman, "				(2) PAGERANK: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#PageRank transformada
arquivo <- read.table("resultados/resultadosRanking/rankingPageRank_transformada_bootstrap1602.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 4, 5, 17, 20, 23, 28, 3, 6, 2, 7, 8, 9, 11, 12, 13, 14, 15, 16, 18, 19, 21, 22, 24, 25, 26, 27, 38, 39, 40, 29, 34, 10, 30,31, 32, 33, 35, 36, 37)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 1602		", kendall,"		", spearman, "				(2) PAGERANK: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Massey original
arquivo <- read.table("resultados/resultadosRanking/rankingMassey_original_bootstrap1602.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 4, 5, 17, 20, 23, 28, 3, 6, 2, 7, 8, 9, 11, 12, 13, 14, 15, 16, 18, 19, 21, 22, 24, 25, 26, 27, 38, 39, 40, 29, 34, 10, 30,31, 32, 33, 35, 36, 37)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 1602		", kendall,"		", spearman, "				(2) MASSEY: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Massey transformada
arquivo <- read.table("resultados/resultadosRanking/rankingMassey_transformada_bootstrap1602.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 4, 5, 17, 20, 23, 28, 3, 6, 2, 7, 8, 9, 11, 12, 13, 14, 15, 16, 18, 19, 21, 22, 24, 25, 26, 27, 38, 39, 40, 29, 34, 10, 30,31, 32, 33, 35, 36, 37)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 1602		", kendall,"		", spearman, "				(2) MASSEY: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Colley original
arquivo <- read.table("resultados/resultadosRanking/rankingColley_original_bootstrap1602.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 4, 5, 17, 20, 23, 28, 3, 6, 2, 7, 8, 9, 11, 12, 13, 14, 15, 16, 18, 19, 21, 22, 24, 25, 26, 27, 38, 39, 40, 29, 34, 10, 30,31, 32, 33, 35, 36, 37)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 1602		", kendall,"		", spearman, "				(2) COLLEY: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Colley original
arquivo <- read.table("resultados/resultadosRanking/rankingColley_transformada_bootstrap1602.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 4, 5, 17, 20, 23, 28, 3, 6, 2, 7, 8, 9, 11, 12, 13, 14, 15, 16, 18, 19, 21, 22, 24, 25, 26, 27, 38, 39, 40, 29, 34, 10, 30,31, 32, 33, 35, 36, 37)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 1602		", kendall,"		", spearman, "				(2) COLLEY: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Louvain + PageRank Original
arquivo <- read.table("resultados/resultadosRanking/rankingLouvain+PageRank_original_bootstrap1602.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 4, 5, 17, 20, 23, 28, 3, 6, 2, 7, 8, 9, 11, 12, 13, 14, 15, 16, 18, 19, 21, 22, 24, 25, 26, 27, 38, 39, 40, 29, 34, 10, 30,31, 32, 33, 35, 36, 37)
oraculo <- head(oraculo, numLinhas)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 1602		", kendall,"		", spearman, "				(3) LOUVAIN + PAGERANK: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Louvain + PageRank transformada
arquivo <- read.table("resultados/resultadosRanking/rankingLouvain+PageRank_transformada_bootstrap1602.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 4, 5, 17, 20, 23, 28, 3, 6, 2, 7, 8, 9, 11, 12, 13, 14, 15, 16, 18, 19, 21, 22, 24, 25, 26, 27, 38, 39, 40, 29, 34, 10, 30,31, 32, 33, 35, 36, 37)
oraculo <- head(oraculo, numLinhas)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 1602		", kendall,"		", spearman, "				(3) LOUVAIN + PAGERANK: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Louvain + Centralidade Original
arquivo <- read.table("resultados/resultadosRanking/rankingLouvain+Centralidade_original_bootstrap1602.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 4, 5, 17, 20, 23, 28, 3, 6, 2, 7, 8, 9, 11, 12, 13, 14, 15, 16, 18, 19, 21, 22, 24, 25, 26, 27, 38, 39, 40, 29, 34, 10, 30,31, 32, 33, 35, 36, 37)
oraculo <- head(oraculo, numLinhas)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 1602		", kendall,"		", spearman, "				(3) LOUVAIN + CENTRALIDADE: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Louvain + Centralidade transformada
arquivo <- read.table("resultados/resultadosRanking/rankingLouvain+Centralidade_transformada_bootstrap1602.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 4, 5, 17, 20, 23, 28, 3, 6, 2, 7, 8, 9, 11, 12, 13, 14, 15, 16, 18, 19, 21, 22, 24, 25, 26, 27, 38, 39, 40, 29, 34, 10, 30,31, 32, 33, 35, 36, 37)
oraculo <- head(oraculo, numLinhas)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 1602		", kendall,"		", spearman, "				(3) LOUVAIN + CENTRALIDADE: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

test<-("\n\n")
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#----------------------------------------------------------------------------------------#
#bootstrap 1997

#SimCosseno original
arquivo <- read.table("resultados/resultadosRanking/rankingSimCosseno_original_bootstrap1997.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 0:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 2, 3, 5, 10, 19, 20, 21, 22, 23, 24, 16, 9, 4, 6, 7, 11, 12, 13, 14, 15, 18, 26, 8, 17, 25)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 1997		", kendall,"		", spearman, "				(1) SIM COSSENO: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#SimCosseno transformada
arquivo <- read.table("resultados/resultadosRanking/rankingSimCosseno_transformada_bootstrap1997.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 2, 3, 5, 10, 19, 20, 21, 22, 23, 24, 16, 9, 4, 6, 7, 11, 12, 13, 14, 15, 18, 26, 8, 17, 25)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 1997		", kendall,"		", spearman, "				(1) SIM COSSENO: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Euclidiana original
arquivo <- read.table("resultados/resultadosRanking/rankingEuclidiana_original_bootstrap1997.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 2, 3, 5, 10, 19, 20, 21, 22, 23, 24, 16, 9, 4, 6, 7, 11, 12, 13, 14, 15, 18, 26, 8, 17, 25)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 1997		", kendall,"		", spearman, "				(1) EUCLIDIANA: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Euclidiana transformada
arquivo <- read.table("resultados/resultadosRanking/rankingEuclidiana_transformada_bootstrap1997.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 2, 3, 5, 10, 19, 20, 21, 22, 23, 24, 16, 9, 4, 6, 7, 11, 12, 13, 14, 15, 18, 26, 8, 17, 25)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 1997		", kendall,"		", spearman, "				(1) EUCLIDIANA: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#PageRank original
arquivo <- read.table("resultados/resultadosRanking/rankingPageRank_original_bootstrap1997.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 2, 3, 5, 10, 19, 20, 21, 22, 23, 24, 16, 9, 4, 6, 7, 11, 12, 13, 14, 15, 18, 26, 8, 17, 25)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 1997		", kendall,"		", spearman, "				(2) PAGERANK: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#PageRank transformada
arquivo <- read.table("resultados/resultadosRanking/rankingPageRank_transformada_bootstrap1997.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 2, 3, 5, 10, 19, 20, 21, 22, 23, 24, 16, 9, 4, 6, 7, 11, 12, 13, 14, 15, 18, 26, 8, 17, 25)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 1997		", kendall,"		", spearman, "				(2) PAGERANK: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Massey original
arquivo <- read.table("resultados/resultadosRanking/rankingMassey_original_bootstrap1997.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 2, 3, 5, 10, 19, 20, 21, 22, 23, 24, 16, 9, 4, 6, 7, 11, 12, 13, 14, 15, 18, 26, 8, 17, 25)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 1997		", kendall,"		", spearman, "				(2) MASSEY: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Massey transformada
arquivo <- read.table("resultados/resultadosRanking/rankingMassey_transformada_bootstrap1997.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 2, 3, 5, 10, 19, 20, 21, 22, 23, 24, 16, 9, 4, 6, 7, 11, 12, 13, 14, 15, 18, 26, 8, 17, 25)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 1997		", kendall,"		", spearman, "				(2) MASSEY: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Colley original
arquivo <- read.table("resultados/resultadosRanking/rankingColley_original_bootstrap1997.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 2, 3, 5, 10, 19, 20, 21, 22, 23, 24, 16, 9, 4, 6, 7, 11, 12, 13, 14, 15, 18, 26, 8, 17, 25)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 1997		", kendall,"		", spearman, "				(2) COLLEY: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Colley original
arquivo <- read.table("resultados/resultadosRanking/rankingColley_transformada_bootstrap1997.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 2, 3, 5, 10, 19, 20, 21, 22, 23, 24, 16, 9, 4, 6, 7, 11, 12, 13, 14, 15, 18, 26, 8, 17, 25)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 1997		", kendall,"		", spearman, "				(2) COLLEY: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Louvain + PageRank Original
arquivo <- read.table("resultados/resultadosRanking/rankingLouvain+PageRank_original_bootstrap1997.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 2, 3, 5, 10, 19, 20, 21, 22, 23, 24, 16, 9, 4, 6, 7, 11, 12, 13, 14, 15, 18, 26, 8, 17, 25)
oraculo <- head(oraculo, numLinhas)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 1997		", kendall,"		", spearman, "				(3) LOUVAIN + PAGERANK: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Louvain + PageRank transformada
arquivo <- read.table("resultados/resultadosRanking/rankingLouvain+PageRank_transformada_bootstrap1997.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 2, 3, 5, 10, 19, 20, 21, 22, 23, 24, 16, 9, 4, 6, 7, 11, 12, 13, 14, 15, 18, 26, 8, 17, 25)
oraculo <- head(oraculo, numLinhas)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 1997		", kendall,"		", spearman, "				(3) LOUVAIN + PAGERANK: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Louvain + Centralidade Original
arquivo <- read.table("resultados/resultadosRanking/rankingLouvain+Centralidade_original_bootstrap1997.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 2, 3, 5, 10, 19, 20, 21, 22, 23, 24, 16, 9, 4, 6, 7, 11, 12, 13, 14, 15, 18, 26, 8, 17, 25)
oraculo <- head(oraculo, numLinhas)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 1997		", kendall,"		", spearman, "				(3) LOUVAIN + CENTRALIDADE: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Louvain + Centralidade transformada
arquivo <- read.table("resultados/resultadosRanking/rankingLouvain+Centralidade_transformada_bootstrap1997.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 2, 3, 5, 10, 19, 20, 21, 22, 23, 24, 16, 9, 4, 6, 7, 11, 12, 13, 14, 15, 18, 26, 8, 17, 25)
oraculo <- head(oraculo, numLinhas)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 1997		", kendall,"		", spearman, "				(3) LOUVAIN + CENTRALIDADE: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

test<-("\n\n")
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)
