test<-("\n\n")
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

# jquery 2145

#SimCosseno original
arquivo <- read.table("resultados/resultadosRanking/rankingSimCosseno_original_jquery2145.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 0:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 14, 2, 9, 12, 13, 15, 16, 17, 23, 24, 26, 27, 28, 33, 37, 3, 4, 5, 6, 7, 10, 11, 20, 25, 29, 31, 35, 38, 39, 8, 18, 22, 30, 32, 34, 19, 21, 36)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("JQUERY 2145		", kendall,"		", spearman, "				(1) SIM COSSENO: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#SimCosseno transformada
arquivo <- read.table("resultados/resultadosRanking/rankingSimCosseno_transformada_jquery2145.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 14, 2, 9, 12, 13, 15, 16, 17, 23, 24, 26, 27, 28, 33, 37, 3, 4, 5, 6, 7, 10, 11, 20, 25, 29, 31, 35, 38, 39, 8, 18, 22, 30, 32, 34, 19, 21, 36)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("JQUERY 2145		", kendall,"		", spearman, "				(1) SIM COSSENO: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Euclidiana original
arquivo <- read.table("resultados/resultadosRanking/rankingEuclidiana_original_jquery2145.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 14, 2, 9, 12, 13, 15, 16, 17, 23, 24, 26, 27, 28, 33, 37, 3, 4, 5, 6, 7, 10, 11, 20, 25, 29, 31, 35, 38, 39, 8, 18, 22, 30, 32, 34, 19, 21, 36)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("JQUERY 2145		", kendall,"		", spearman, "				(1) EUCLIDIANA: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Euclidiana transformada
arquivo <- read.table("resultados/resultadosRanking/rankingEuclidiana_transformada_jquery2145.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 14, 2, 9, 12, 13, 15, 16, 17, 23, 24, 26, 27, 28, 33, 37, 3, 4, 5, 6, 7, 10, 11, 20, 25, 29, 31, 35, 38, 39, 8, 18, 22, 30, 32, 34, 19, 21, 36)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("JQUERY 2145		", kendall,"		", spearman, "				(1) EUCLIDIANA: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#PageRank original
arquivo <- read.table("resultados/resultadosRanking/rankingPageRank_original_jquery2145.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 14, 2, 9, 12, 13, 15, 16, 17, 23, 24, 26, 27, 28, 33, 37, 3, 4, 5, 6, 7, 10, 11, 20, 25, 29, 31, 35, 38, 39, 8, 18, 22, 30, 32, 34, 19, 21, 36)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("JQUERY 2145		", kendall,"		", spearman, "				(2) PAGERANK: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#PageRank transformada
arquivo <- read.table("resultados/resultadosRanking/rankingPageRank_transformada_jquery2145.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 14, 2, 9, 12, 13, 15, 16, 17, 23, 24, 26, 27, 28, 33, 37, 3, 4, 5, 6, 7, 10, 11, 20, 25, 29, 31, 35, 38, 39, 8, 18, 22, 30, 32, 34, 19, 21, 36)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("JQUERY 2145		", kendall,"		", spearman, "				(2) PAGERANK: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Massey original
arquivo <- read.table("resultados/resultadosRanking/rankingMassey_original_jquery2145.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 14, 2, 9, 12, 13, 15, 16, 17, 23, 24, 26, 27, 28, 33, 37, 3, 4, 5, 6, 7, 10, 11, 20, 25, 29, 31, 35, 38, 39, 8, 18, 22, 30, 32, 34, 19, 21, 36)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("JQUERY 2145		", kendall,"		", spearman, "				(2) MASSEY: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Massey transformada
arquivo <- read.table("resultados/resultadosRanking/rankingMassey_transformada_jquery2145.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 14, 2, 9, 12, 13, 15, 16, 17, 23, 24, 26, 27, 28, 33, 37, 3, 4, 5, 6, 7, 10, 11, 20, 25, 29, 31, 35, 38, 39, 8, 18, 22, 30, 32, 34, 19, 21, 36)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("JQUERY 2145		", kendall,"		", spearman, "				(2) MASSEY: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Colley original
arquivo <- read.table("resultados/resultadosRanking/rankingColley_original_jquery2145.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 14, 2, 9, 12, 13, 15, 16, 17, 23, 24, 26, 27, 28, 33, 37, 3, 4, 5, 6, 7, 10, 11, 20, 25, 29, 31, 35, 38, 39, 8, 18, 22, 30, 32, 34, 19, 21, 36)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("JQUERY 2145		", kendall,"		", spearman, "				(2) COLLEY: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Colley original
arquivo <- read.table("resultados/resultadosRanking/rankingColley_transformada_jquery2145.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 14, 2, 9, 12, 13, 15, 16, 17, 23, 24, 26, 27, 28, 33, 37, 3, 4, 5, 6, 7, 10, 11, 20, 25, 29, 31, 35, 38, 39, 8, 18, 22, 30, 32, 34, 19, 21, 36)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("JQUERY 2145		", kendall,"		", spearman, "				(2) COLLEY: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Louvain + PageRank Original
arquivo <- read.table("resultados/resultadosRanking/rankingLouvain+PageRank_original_jquery2145.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 14, 2, 9, 12, 13, 15, 16, 17, 23, 24, 26, 27, 28, 33, 37, 3, 4, 5, 6, 7, 10, 11, 20, 25, 29, 31, 35, 38, 39, 8, 18, 22, 30, 32, 34, 19, 21, 36)
oraculo <- head(oraculo, numLinhas)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("JQUERY 2145		", kendall,"		", spearman, "				(3) LOUVAIN + PAGERANK: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Louvain + PageRank transformada
arquivo <- read.table("resultados/resultadosRanking/rankingLouvain+PageRank_transformada_jquery2145.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 14, 2, 9, 12, 13, 15, 16, 17, 23, 24, 26, 27, 28, 33, 37, 3, 4, 5, 6, 7, 10, 11, 20, 25, 29, 31, 35, 38, 39, 8, 18, 22, 30, 32, 34, 19, 21, 36)
oraculo <- head(oraculo, numLinhas)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("JQUERY 2145		", kendall,"		", spearman, "				(3) LOUVAIN + PAGERANK: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Louvain + Centralidade Original
arquivo <- read.table("resultados/resultadosRanking/rankingLouvain+Centralidade_original_jquery2145.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 14, 2, 9, 12, 13, 15, 16, 17, 23, 24, 26, 27, 28, 33, 37, 3, 4, 5, 6, 7, 10, 11, 20, 25, 29, 31, 35, 38, 39, 8, 18, 22, 30, 32, 34, 19, 21, 36)
oraculo <- head(oraculo, numLinhas)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("JQUERY 2145		", kendall,"		", spearman, "				(3) LOUVAIN + CENTRALIDADE: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Louvain + Centralidade transformada
arquivo <- read.table("resultados/resultadosRanking/rankingLouvain+Centralidade_transformada_jquery2145.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 14, 2, 9, 12, 13, 15, 16, 17, 23, 24, 26, 27, 28, 33, 37, 3, 4, 5, 6, 7, 10, 11, 20, 25, 29, 31, 35, 38, 39, 8, 18, 22, 30, 32, 34, 19, 21, 36)
oraculo <- head(oraculo, numLinhas)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("JQUERY 2145		", kendall,"		", spearman, "				(3) LOUVAIN + CENTRALIDADE: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

test<-("\n\n")
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#----------------------------------------------------------------------------------------#
# jquery 2310

#SimCosseno original
arquivo <- read.table("resultados/resultadosRanking/rankingSimCosseno_original_jquery2310.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 0:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 4, 30, 37, 1, 5, 10, 13, 14, 17, 18, 19, 20, 21, 25, 26, 27, 31, 34, 36, 38, 2, 3, 7, 12, 15, 23, 24, 29, 32, 33, 6, 8, 11, 9,16, 22, 28, 35)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("JQUERY 2310		", kendall,"		", spearman, "				(1) SIM COSSENO: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#SimCosseno transformada
arquivo <- read.table("resultados/resultadosRanking/rankingSimCosseno_transformada_jquery2310.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 4, 30, 37, 1, 5, 10, 13, 14, 17, 18, 19, 20, 21, 25, 26, 27, 31, 34, 36, 38, 2, 3, 7, 12, 15, 23, 24, 29, 32, 33, 6, 8, 11, 9,16, 22, 28, 35)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("JQUERY 2310		", kendall,"		", spearman, "				(1) SIM COSSENO: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Euclidiana original
arquivo <- read.table("resultados/resultadosRanking/rankingEuclidiana_original_jquery2310.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 4, 30, 37, 1, 5, 10, 13, 14, 17, 18, 19, 20, 21, 25, 26, 27, 31, 34, 36, 38, 2, 3, 7, 12, 15, 23, 24, 29, 32, 33, 6, 8, 11, 9,16, 22, 28, 35)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("JQUERY 2310		", kendall,"		", spearman, "				(1) EUCLIDIANA: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Euclidiana transformada
arquivo <- read.table("resultados/resultadosRanking/rankingEuclidiana_transformada_jquery2310.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 4, 30, 37, 1, 5, 10, 13, 14, 17, 18, 19, 20, 21, 25, 26, 27, 31, 34, 36, 38, 2, 3, 7, 12, 15, 23, 24, 29, 32, 33, 6, 8, 11, 9,16, 22, 28, 35)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("JQUERY 2310		", kendall,"		", spearman, "				(1) EUCLIDIANA: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#PageRank original
arquivo <- read.table("resultados/resultadosRanking/rankingPageRank_original_jquery2310.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 4, 30, 37, 1, 5, 10, 13, 14, 17, 18, 19, 20, 21, 25, 26, 27, 31, 34, 36, 38, 2, 3, 7, 12, 15, 23, 24, 29, 32, 33, 6, 8, 11, 9,16, 22, 28, 35)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("JQUERY 2310		", kendall,"		", spearman, "				(2) PAGERANK: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#PageRank transformada
arquivo <- read.table("resultados/resultadosRanking/rankingPageRank_transformada_jquery2310.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 4, 30, 37, 1, 5, 10, 13, 14, 17, 18, 19, 20, 21, 25, 26, 27, 31, 34, 36, 38, 2, 3, 7, 12, 15, 23, 24, 29, 32, 33, 6, 8, 11, 9,16, 22, 28, 35)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("JQUERY 2310		", kendall,"		", spearman, "				(2) PAGERANK: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Massey original
arquivo <- read.table("resultados/resultadosRanking/rankingMassey_original_jquery2310.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 4, 30, 37, 1, 5, 10, 13, 14, 17, 18, 19, 20, 21, 25, 26, 27, 31, 34, 36, 38, 2, 3, 7, 12, 15, 23, 24, 29, 32, 33, 6, 8, 11, 9,16, 22, 28, 35)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("JQUERY 2310		", kendall,"		", spearman, "				(2) MASSEY: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Massey transformada
arquivo <- read.table("resultados/resultadosRanking/rankingMassey_transformada_jquery2310.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 4, 30, 37, 1, 5, 10, 13, 14, 17, 18, 19, 20, 21, 25, 26, 27, 31, 34, 36, 38, 2, 3, 7, 12, 15, 23, 24, 29, 32, 33, 6, 8, 11, 9,16, 22, 28, 35)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("JQUERY 2310		", kendall,"		", spearman, "				(2) MASSEY: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Colley original
arquivo <- read.table("resultados/resultadosRanking/rankingColley_original_jquery2310.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 4, 30, 37, 1, 5, 10, 13, 14, 17, 18, 19, 20, 21, 25, 26, 27, 31, 34, 36, 38, 2, 3, 7, 12, 15, 23, 24, 29, 32, 33, 6, 8, 11, 9,16, 22, 28, 35)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("JQUERY 2310		", kendall,"		", spearman, "				(2) COLLEY: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Colley original
arquivo <- read.table("resultados/resultadosRanking/rankingColley_transformada_jquery2310.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 4, 30, 37, 1, 5, 10, 13, 14, 17, 18, 19, 20, 21, 25, 26, 27, 31, 34, 36, 38, 2, 3, 7, 12, 15, 23, 24, 29, 32, 33, 6, 8, 11, 9,16, 22, 28, 35)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("JQUERY 2310		", kendall,"		", spearman, "				(2) COLLEY: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Louvain + PageRank Original
arquivo <- read.table("resultados/resultadosRanking/rankingLouvain+PageRank_original_jquery2310.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 4, 30, 37, 1, 5, 10, 13, 14, 17, 18, 19, 20, 21, 25, 26, 27, 31, 34, 36, 38, 2, 3, 7, 12, 15, 23, 24, 29, 32, 33, 6, 8, 11, 9,16, 22, 28, 35)
oraculo <- head(oraculo, numLinhas)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("JQUERY 2310		", kendall,"		", spearman, "				(3) LOUVAIN + PAGERANK: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Louvain + PageRank transformada
arquivo <- read.table("resultados/resultadosRanking/rankingLouvain+PageRank_transformada_jquery2310.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 4, 30, 37, 1, 5, 10, 13, 14, 17, 18, 19, 20, 21, 25, 26, 27, 31, 34, 36, 38, 2, 3, 7, 12, 15, 23, 24, 29, 32, 33, 6, 8, 11, 9,16, 22, 28, 35)
oraculo <- head(oraculo, numLinhas)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("JQUERY 2310		", kendall,"		", spearman, "				(3) LOUVAIN + PAGERANK: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Louvain + Centralidade Original
arquivo <- read.table("resultados/resultadosRanking/rankingLouvain+Centralidade_original_jquery2310.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 4, 30, 37, 1, 5, 10, 13, 14, 17, 18, 19, 20, 21, 25, 26, 27, 31, 34, 36, 38, 2, 3, 7, 12, 15, 23, 24, 29, 32, 33, 6, 8, 11, 9,16, 22, 28, 35)
oraculo <- head(oraculo, numLinhas)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("JQUERY 2310		", kendall,"		", spearman, "				(3) LOUVAIN + CENTRALIDADE: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Louvain + Centralidade transformada
arquivo <- read.table("resultados/resultadosRanking/rankingLouvain+Centralidade_transformada_jquery2310.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 4, 30, 37, 1, 5, 10, 13, 14, 17, 18, 19, 20, 21, 25, 26, 27, 31, 34, 36, 38, 2, 3, 7, 12, 15, 23, 24, 29, 32, 33, 6, 8, 11, 9,16, 22, 28, 35)
oraculo <- head(oraculo, numLinhas)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("JQUERY 2310		", kendall,"		", spearman, "				(3) LOUVAIN + CENTRALIDADE: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

test<-("\n\n")
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#----------------------------------------------------------------------------------------#
# jquery 2199


#SimCosseno original
arquivo <- read.table("resultados/resultadosRanking/rankingSimCosseno_original_jquery2199.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 0:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 7, 9, 12, 15, 16, 19, 20, 3, 4, 6, 8, 10, 11, 13, 17, 18, 2, 5, 14)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("JQUERY 2199		", kendall,"		", spearman, "				(1) SIM COSSENO: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#SimCosseno transformada
arquivo <- read.table("resultados/resultadosRanking/rankingSimCosseno_transformada_jquery2199.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 7, 9, 12, 15, 16, 19, 20, 3, 4, 6, 8, 10, 11, 13, 17, 18, 2, 5, 14)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("JQUERY 2199		", kendall,"		", spearman, "				(1) SIM COSSENO: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Euclidiana original
arquivo <- read.table("resultados/resultadosRanking/rankingEuclidiana_original_jquery2199.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 7, 9, 12, 15, 16, 19, 20, 3, 4, 6, 8, 10, 11, 13, 17, 18, 2, 5, 14)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("JQUERY 2199		", kendall,"		", spearman, "				(1) EUCLIDIANA: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Euclidiana transformada
arquivo <- read.table("resultados/resultadosRanking/rankingEuclidiana_transformada_jquery2199.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 7, 9, 12, 15, 16, 19, 20, 3, 4, 6, 8, 10, 11, 13, 17, 18, 2, 5, 14)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("JQUERY 2199		", kendall,"		", spearman, "				(1) EUCLIDIANA: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#PageRank original
arquivo <- read.table("resultados/resultadosRanking/rankingPageRank_original_jquery2199.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 7, 9, 12, 15, 16, 19, 20, 3, 4, 6, 8, 10, 11, 13, 17, 18, 2, 5, 14)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("JQUERY 2199		", kendall,"		", spearman, "				(2) PAGERANK: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#PageRank transformada
arquivo <- read.table("resultados/resultadosRanking/rankingPageRank_transformada_jquery2199.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 7, 9, 12, 15, 16, 19, 20, 3, 4, 6, 8, 10, 11, 13, 17, 18, 2, 5, 14)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("JQUERY 2199		", kendall,"		", spearman, "				(2) PAGERANK: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Massey original
arquivo <- read.table("resultados/resultadosRanking/rankingMassey_original_jquery2199.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 7, 9, 12, 15, 16, 19, 20, 3, 4, 6, 8, 10, 11, 13, 17, 18, 2, 5, 14)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("JQUERY 2199		", kendall,"		", spearman, "				(2) MASSEY: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Massey transformada
arquivo <- read.table("resultados/resultadosRanking/rankingMassey_transformada_jquery2199.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 7, 9, 12, 15, 16, 19, 20, 3, 4, 6, 8, 10, 11, 13, 17, 18, 2, 5, 14)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("JQUERY 2199		", kendall,"		", spearman, "				(2) MASSEY: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Colley original
arquivo <- read.table("resultados/resultadosRanking/rankingColley_original_jquery2199.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 7, 9, 12, 15, 16, 19, 20, 3, 4, 6, 8, 10, 11, 13, 17, 18, 2, 5, 14)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("JQUERY 2199		", kendall,"		", spearman, "				(2) COLLEY: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Colley original
arquivo <- read.table("resultados/resultadosRanking/rankingColley_transformada_jquery2199.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 7, 9, 12, 15, 16, 19, 20, 3, 4, 6, 8, 10, 11, 13, 17, 18, 2, 5, 14)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("JQUERY 2199		", kendall,"		", spearman, "				(2) COLLEY: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Louvain + PageRank Original
arquivo <- read.table("resultados/resultadosRanking/rankingLouvain+PageRank_original_jquery2199.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 7, 9, 12, 15, 16, 19, 20, 3, 4, 6, 8, 10, 11, 13, 17, 18, 2, 5, 14)
oraculo <- head(oraculo, numLinhas)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("JQUERY 2199		", kendall,"		", spearman, "				(3) LOUVAIN + PAGERANK: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Louvain + PageRank transformada
arquivo <- read.table("resultados/resultadosRanking/rankingLouvain+PageRank_transformada_jquery2199.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 7, 9, 12, 15, 16, 19, 20, 3, 4, 6, 8, 10, 11, 13, 17, 18, 2, 5, 14)
oraculo <- head(oraculo, numLinhas)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("JQUERY 2199		", kendall,"		", spearman, "				(3) LOUVAIN + PAGERANK: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Louvain + Centralidade Original
arquivo <- read.table("resultados/resultadosRanking/rankingLouvain+Centralidade_original_jquery2199.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 7, 9, 12, 15, 16, 19, 20, 3, 4, 6, 8, 10, 11, 13, 17, 18, 2, 5, 14)
oraculo <- head(oraculo, numLinhas)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("JQUERY 2199		", kendall,"		", spearman, "				(3) LOUVAIN + CENTRALIDADE: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Louvain + Centralidade transformada
arquivo <- read.table("resultados/resultadosRanking/rankingLouvain+Centralidade_transformada_jquery2199.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 7, 9, 12, 15, 16, 19, 20, 3, 4, 6, 8, 10, 11, 13, 17, 18, 2, 5, 14)
oraculo <- head(oraculo, numLinhas)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("JQUERY 2199		", kendall,"		", spearman, "				(3) LOUVAIN + CENTRALIDADE: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

test<-("\n\n")
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#----------------------------------------------------------------------------------------#
# jquery 2321

#SimCosseno original
arquivo <- read.table("resultados/resultadosRanking/rankingSimCosseno_original_jquery2321.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 0:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 2, 17, 21, 3, 4, 5, 8, 10, 11, 12, 13, 16, 18, 19, 20, 22, 6, 7, 14, 15, 9)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("JQUERY 2321		", kendall,"		", spearman, "				(1) SIM COSSENO: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#SimCosseno transformada
arquivo <- read.table("resultados/resultadosRanking/rankingSimCosseno_transformada_jquery2321.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 2, 17, 21, 3, 4, 5, 8, 10, 11, 12, 13, 16, 18, 19, 20, 22, 6, 7, 14, 15, 9)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("JQUERY 2321		", kendall,"		", spearman, "				(1) SIM COSSENO: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Euclidiana original
arquivo <- read.table("resultados/resultadosRanking/rankingEuclidiana_original_jquery2321.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 2, 17, 21, 3, 4, 5, 8, 10, 11, 12, 13, 16, 18, 19, 20, 22, 6, 7, 14, 15, 9)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("JQUERY 2321		", kendall,"		", spearman, "				(1) EUCLIDIANA: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Euclidiana transformada
arquivo <- read.table("resultados/resultadosRanking/rankingEuclidiana_transformada_jquery2321.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 2, 17, 21, 3, 4, 5, 8, 10, 11, 12, 13, 16, 18, 19, 20, 22, 6, 7, 14, 15, 9)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("JQUERY 2321		", kendall,"		", spearman, "				(1) EUCLIDIANA: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#PageRank original
arquivo <- read.table("resultados/resultadosRanking/rankingPageRank_original_jquery2321.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 2, 17, 21, 3, 4, 5, 8, 10, 11, 12, 13, 16, 18, 19, 20, 22, 6, 7, 14, 15, 9)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("JQUERY 2321		", kendall,"		", spearman, "				(2) PAGERANK: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#PageRank transformada
arquivo <- read.table("resultados/resultadosRanking/rankingPageRank_transformada_jquery2321.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 2, 17, 21, 3, 4, 5, 8, 10, 11, 12, 13, 16, 18, 19, 20, 22, 6, 7, 14, 15, 9)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("JQUERY 2321		", kendall,"		", spearman, "				(2) PAGERANK: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Massey original
arquivo <- read.table("resultados/resultadosRanking/rankingMassey_original_jquery2321.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 2, 17, 21, 3, 4, 5, 8, 10, 11, 12, 13, 16, 18, 19, 20, 22, 6, 7, 14, 15, 9)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("JQUERY 2321		", kendall,"		", spearman, "				(2) MASSEY: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Massey transformada
arquivo <- read.table("resultados/resultadosRanking/rankingMassey_transformada_jquery2321.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 2, 17, 21, 3, 4, 5, 8, 10, 11, 12, 13, 16, 18, 19, 20, 22, 6, 7, 14, 15, 9)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("JQUERY 2321		", kendall,"		", spearman, "				(2) MASSEY: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Colley original
arquivo <- read.table("resultados/resultadosRanking/rankingColley_original_jquery2321.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 2, 17, 21, 3, 4, 5, 8, 10, 11, 12, 13, 16, 18, 19, 20, 22, 6, 7, 14, 15, 9)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("JQUERY 2321		", kendall,"		", spearman, "				(2) COLLEY: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Colley original
arquivo <- read.table("resultados/resultadosRanking/rankingColley_transformada_jquery2321.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 2, 17, 21, 3, 4, 5, 8, 10, 11, 12, 13, 16, 18, 19, 20, 22, 6, 7, 14, 15, 9)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("JQUERY 2321		", kendall,"		", spearman, "				(2) COLLEY: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Louvain + PageRank Original
arquivo <- read.table("resultados/resultadosRanking/rankingLouvain+PageRank_original_jquery2321.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 2, 17, 21, 3, 4, 5, 8, 10, 11, 12, 13, 16, 18, 19, 20, 22, 6, 7, 14, 15, 9)
oraculo <- head(oraculo, numLinhas)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("JQUERY 2321		", kendall,"		", spearman, "				(3) LOUVAIN + PAGERANK: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Louvain + PageRank transformada
arquivo <- read.table("resultados/resultadosRanking/rankingLouvain+PageRank_transformada_jquery2321.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 2, 17, 21, 3, 4, 5, 8, 10, 11, 12, 13, 16, 18, 19, 20, 22, 6, 7, 14, 15, 9)
oraculo <- head(oraculo, numLinhas)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("JQUERY 2321		", kendall,"		", spearman, "				(3) LOUVAIN + PAGERANK: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Louvain + Centralidade Original
arquivo <- read.table("resultados/resultadosRanking/rankingLouvain+Centralidade_original_jquery2321.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 2, 17, 21, 3, 4, 5, 8, 10, 11, 12, 13, 16, 18, 19, 20, 22, 6, 7, 14, 15, 9)
oraculo <- head(oraculo, numLinhas)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("JQUERY 2321		", kendall,"		", spearman, "				(3) LOUVAIN + CENTRALIDADE: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Louvain + Centralidade transformada
arquivo <- read.table("resultados/resultadosRanking/rankingLouvain+Centralidade_transformada_jquery2321.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 2, 17, 21, 3, 4, 5, 8, 10, 11, 12, 13, 16, 18, 19, 20, 22, 6, 7, 14, 15, 9)
oraculo <- head(oraculo, numLinhas)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("JQUERY 2321		", kendall,"		", spearman, "				(3) LOUVAIN + CENTRALIDADE: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

test<-("\n\n")
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#----------------------------------------------------------------------------------------#

#jquery 1692

#SimCosseno original
arquivo <- read.table("resultados/resultadosRanking/rankingSimCosseno_original_jquery1692.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 0:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 6, 8, 10, 11, 14, 17, 21, 26, 28, 4, 7, 9, 12, 13, 18, 19, 20, 22, 23, 24, 25, 29, 30, 31, 2, 3, 16, 27, 32, 33, 5, 15)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("JQUERY 1692		", kendall,"		", spearman, "				(1) SIM COSSENO: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#SimCosseno transformada
arquivo <- read.table("resultados/resultadosRanking/rankingSimCosseno_transformada_jquery1692.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 6, 8, 10, 11, 14, 17, 21, 26, 28, 4, 7, 9, 12, 13, 18, 19, 20, 22, 23, 24, 25, 29, 30, 31, 2, 3, 16, 27, 32, 33, 5, 15)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("JQUERY 1692		", kendall,"		", spearman, "				(1) SIM COSSENO: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Euclidiana original
arquivo <- read.table("resultados/resultadosRanking/rankingEuclidiana_original_jquery1692.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 6, 8, 10, 11, 14, 17, 21, 26, 28, 4, 7, 9, 12, 13, 18, 19, 20, 22, 23, 24, 25, 29, 30, 31, 2, 3, 16, 27, 32, 33, 5, 15)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("JQUERY 1692		", kendall,"		", spearman, "				(1) EUCLIDIANA: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Euclidiana transformada
arquivo <- read.table("resultados/resultadosRanking/rankingEuclidiana_transformada_jquery1692.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 6, 8, 10, 11, 14, 17, 21, 26, 28, 4, 7, 9, 12, 13, 18, 19, 20, 22, 23, 24, 25, 29, 30, 31, 2, 3, 16, 27, 32, 33, 5, 15)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("JQUERY 1692		", kendall,"		", spearman, "				(1) EUCLIDIANA: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#PageRank original
arquivo <- read.table("resultados/resultadosRanking/rankingPageRank_original_jquery1692.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 6, 8, 10, 11, 14, 17, 21, 26, 28, 4, 7, 9, 12, 13, 18, 19, 20, 22, 23, 24, 25, 29, 30, 31, 2, 3, 16, 27, 32, 33, 5, 15)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("JQUERY 1692		", kendall,"		", spearman, "				(2) PAGERANK: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#PageRank transformada
arquivo <- read.table("resultados/resultadosRanking/rankingPageRank_transformada_jquery1692.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 6, 8, 10, 11, 14, 17, 21, 26, 28, 4, 7, 9, 12, 13, 18, 19, 20, 22, 23, 24, 25, 29, 30, 31, 2, 3, 16, 27, 32, 33, 5, 15)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("JQUERY 1692		", kendall,"		", spearman, "				(2) PAGERANK: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Massey original
arquivo <- read.table("resultados/resultadosRanking/rankingMassey_original_jquery1692.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 6, 8, 10, 11, 14, 17, 21, 26, 28, 4, 7, 9, 12, 13, 18, 19, 20, 22, 23, 24, 25, 29, 30, 31, 2, 3, 16, 27, 32, 33, 5, 15)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("JQUERY 1692		", kendall,"		", spearman, "				(2) MASSEY: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Massey transformada
arquivo <- read.table("resultados/resultadosRanking/rankingMassey_transformada_jquery1692.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 6, 8, 10, 11, 14, 17, 21, 26, 28, 4, 7, 9, 12, 13, 18, 19, 20, 22, 23, 24, 25, 29, 30, 31, 2, 3, 16, 27, 32, 33, 5, 15)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("JQUERY 1692		", kendall,"		", spearman, "				(2) MASSEY: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Colley original
arquivo <- read.table("resultados/resultadosRanking/rankingColley_original_jquery1692.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 6, 8, 10, 11, 14, 17, 21, 26, 28, 4, 7, 9, 12, 13, 18, 19, 20, 22, 23, 24, 25, 29, 30, 31, 2, 3, 16, 27, 32, 33, 5, 15)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("JQUERY 1692		", kendall,"		", spearman, "				(2) COLLEY: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Colley original
arquivo <- read.table("resultados/resultadosRanking/rankingColley_transformada_jquery1692.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 6, 8, 10, 11, 14, 17, 21, 26, 28, 4, 7, 9, 12, 13, 18, 19, 20, 22, 23, 24, 25, 29, 30, 31, 2, 3, 16, 27, 32, 33, 5, 15)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("JQUERY 1692		", kendall,"		", spearman, "				(2) COLLEY: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Louvain + PageRank Original
arquivo <- read.table("resultados/resultadosRanking/rankingLouvain+PageRank_original_jquery1692.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 6, 8, 10, 11, 14, 17, 21, 26, 28, 4, 7, 9, 12, 13, 18, 19, 20, 22, 23, 24, 25, 29, 30, 31, 2, 3, 16, 27, 32, 33, 5, 15)
oraculo <- head(oraculo, numLinhas)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("JQUERY 1692		", kendall,"		", spearman, "				(3) LOUVAIN + PAGERANK: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Louvain + PageRank transformada
arquivo <- read.table("resultados/resultadosRanking/rankingLouvain+PageRank_transformada_jquery1692.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 6, 8, 10, 11, 14, 17, 21, 26, 28, 4, 7, 9, 12, 13, 18, 19, 20, 22, 23, 24, 25, 29, 30, 31, 2, 3, 16, 27, 32, 33, 5, 15)
oraculo <- head(oraculo, numLinhas)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("JQUERY 1692		", kendall,"		", spearman, "				(3) LOUVAIN + PAGERANK: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Louvain + Centralidade Original
arquivo <- read.table("resultados/resultadosRanking/rankingLouvain+Centralidade_original_jquery1692.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 6, 8, 10, 11, 14, 17, 21, 26, 28, 4, 7, 9, 12, 13, 18, 19, 20, 22, 23, 24, 25, 29, 30, 31, 2, 3, 16, 27, 32, 33, 5, 15)
oraculo <- head(oraculo, numLinhas)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("JQUERY 1692		", kendall,"		", spearman, "				(3) LOUVAIN + CENTRALIDADE: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Louvain + Centralidade transformada
arquivo <- read.table("resultados/resultadosRanking/rankingLouvain+Centralidade_transformada_jquery1692.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 6, 8, 10, 11, 14, 17, 21, 26, 28, 4, 7, 9, 12, 13, 18, 19, 20, 22, 23, 24, 25, 29, 30, 31, 2, 3, 16, 27, 32, 33, 5, 15)
oraculo <- head(oraculo, numLinhas)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("JQUERY 1692		", kendall,"		", spearman, "				(3) LOUVAIN + CENTRALIDADE: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

test<-("\n\n")
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)
