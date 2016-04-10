string = "ARQUIVO			 	 KENDALL				 SPEARMAN						ESTUDO"
write(string, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)
test<-("\n")
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#--------------------------------------------------------------------------------------------------------------------#
#angular_2895

#SimCosseno original
arquivo <- read.table("resultados/resultadosRanking/rankingSimCosseno_original_angular2895.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 0:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 28, 1, 17, 18, 20, 23, 27, 33, 2 , 3, 4, 6, 7, 8, 10, 11, 13, 14, 21, 22, 24, 25, 26, 29, 30, 32, 34, 9, 12, 15, 16, 19, 31, 35, 5)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 2895		", kendall,"		", spearman, "				(1) SIM COSSENO: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#SimCosseno transformada
arquivo <- read.table("resultados/resultadosRanking/rankingSimCosseno_transformada_angular2895.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 28, 1, 17, 18, 20, 23, 27, 33, 2 , 3, 4, 6, 7, 8, 10, 11, 13, 14, 21, 22, 24, 25, 26, 29, 30, 32, 34, 9, 12, 15, 16, 19, 31, 35, 5)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 2895		", kendall,"		", spearman, "				(1) SIM COSSENO: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Euclidiana original
arquivo <- read.table("resultados/resultadosRanking/rankingEuclidiana_original_angular2895.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 28, 1, 17, 18, 20, 23, 27, 33, 2 , 3, 4, 6, 7, 8, 10, 11, 13, 14, 21, 22, 24, 25, 26, 29, 30, 32, 34, 9, 12, 15, 16, 19, 31, 35, 5)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 2895		", kendall,"		", spearman, "				(1) EUCLIDIANA: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Euclidiana transformada
arquivo <- read.table("resultados/resultadosRanking/rankingEuclidiana_transformada_angular2895.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 28, 1, 17, 18, 20, 23, 27, 33, 2 , 3, 4, 6, 7, 8, 10, 11, 13, 14, 21, 22, 24, 25, 26, 29, 30, 32, 34, 9, 12, 15, 16, 19, 31, 35, 5)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 2895		", kendall,"		", spearman, "				(1) EUCLIDIANA: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#PageRank original
arquivo <- read.table("resultados/resultadosRanking/rankingPageRank_original_angular2895.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 28, 1, 17, 18, 20, 23, 27, 33, 2 , 3, 4, 6, 7, 8, 10, 11, 13, 14, 21, 22, 24, 25, 26, 29, 30, 32, 34, 9, 12, 15, 16, 19, 31, 35, 5)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 2895		", kendall,"		", spearman, "				(2) PAGERANK: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#PageRank transformada
arquivo <- read.table("resultados/resultadosRanking/rankingPageRank_transformada_angular2895.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 28, 1, 17, 18, 20, 23, 27, 33, 2 , 3, 4, 6, 7, 8, 10, 11, 13, 14, 21, 22, 24, 25, 26, 29, 30, 32, 34, 9, 12, 15, 16, 19, 31, 35, 5)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 2895		", kendall,"		", spearman, "				(2) PAGERANK: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Massey original
arquivo <- read.table("resultados/resultadosRanking/rankingMassey_original_angular2895.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 28, 1, 17, 18, 20, 23, 27, 33, 2 , 3, 4, 6, 7, 8, 10, 11, 13, 14, 21, 22, 24, 25, 26, 29, 30, 32, 34, 9, 12, 15, 16, 19, 31, 35, 5)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 2895		", kendall,"		", spearman, "				(2) MASSEY: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Massey transformada
arquivo <- read.table("resultados/resultadosRanking/rankingMassey_transformada_angular2895.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 28, 1, 17, 18, 20, 23, 27, 33, 2 , 3, 4, 6, 7, 8, 10, 11, 13, 14, 21, 22, 24, 25, 26, 29, 30, 32, 34, 9, 12, 15, 16, 19, 31, 35, 5)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 2895		", kendall,"		", spearman, "				(2) MASSEY: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Colley original
arquivo <- read.table("resultados/resultadosRanking/rankingColley_original_angular2895.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 28, 1, 17, 18, 20, 23, 27, 33, 2 , 3, 4, 6, 7, 8, 10, 11, 13, 14, 21, 22, 24, 25, 26, 29, 30, 32, 34, 9, 12, 15, 16, 19, 31, 35, 5)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 2895		", kendall,"		", spearman, "				(2) COLLEY: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Colley original
arquivo <- read.table("resultados/resultadosRanking/rankingColley_transformada_angular2895.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 28, 1, 17, 18, 20, 23, 27, 33, 2 , 3, 4, 6, 7, 8, 10, 11, 13, 14, 21, 22, 24, 25, 26, 29, 30, 32, 34, 9, 12, 15, 16, 19, 31, 35, 5)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 2895		", kendall,"		", spearman, "				(2) COLLEY: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Louvain + PageRank Original
arquivo <- read.table("resultados/resultadosRanking/rankingLouvain+PageRank_original_angular2895.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 28, 1, 17, 18, 20, 23, 27, 33, 2 , 3, 4, 6, 7, 8, 10, 11, 13, 14, 21, 22, 24, 25, 26, 29, 30, 32, 34, 9, 12, 15, 16, 19, 31, 35, 5)
oraculo <- head(oraculo, numLinhas)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 2895		", kendall,"		", spearman, "				(3) LOUVAIN + PAGERANK: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Louvain + PageRank transformada
arquivo <- read.table("resultados/resultadosRanking/rankingLouvain+PageRank_transformada_angular2895.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 28, 1, 17, 18, 20, 23, 27, 33, 2 , 3, 4, 6, 7, 8, 10, 11, 13, 14, 21, 22, 24, 25, 26, 29, 30, 32, 34, 9, 12, 15, 16, 19, 31, 35, 5)
oraculo <- head(oraculo, numLinhas)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 2895		", kendall,"		", spearman, "				(3) LOUVAIN + PAGERANK: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Louvain + Centralidade Original
arquivo <- read.table("resultados/resultadosRanking/rankingLouvain+Centralidade_original_angular2895.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 28, 1, 17, 18, 20, 23, 27, 33, 2 , 3, 4, 6, 7, 8, 10, 11, 13, 14, 21, 22, 24, 25, 26, 29, 30, 32, 34, 9, 12, 15, 16, 19, 31, 35, 5)
oraculo <- head(oraculo, numLinhas)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 2895		", kendall,"		", spearman, "				(3) LOUVAIN + CENTRALIDADE: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Louvain + Centralidade transformada
arquivo <- read.table("resultados/resultadosRanking/rankingLouvain+Centralidade_transformada_angular2895.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 28, 1, 17, 18, 20, 23, 27, 33, 2 , 3, 4, 6, 7, 8, 10, 11, 13, 14, 21, 22, 24, 25, 26, 29, 30, 32, 34, 9, 12, 15, 16, 19, 31, 35, 5)
oraculo <- head(oraculo, numLinhas)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 2895		", kendall,"		", spearman, "				(3) LOUVAIN + CENTRALIDADE: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

test<-("\n\n")
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)


#--------------------------------------------------------------------------------------------------------------------#
#angular_734

#SimCosseno original
arquivo <- read.table("resultados/resultadosRanking/rankingSimCosseno_original_angular734.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 0:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 4, 5, 36, 2, 12, 22, 25, 26, 39, 8, 10, 34, 6, 19, 28, 32, 35, 38, 3, 7, 9, 11, 13, 14, 15, 17, 18, 21, 23, 24, 29, 30, 33, 20, 27, 31, 16, 37)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 734		", kendall,"		", spearman, "				(1) SIM COSSENO: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)


#SimCosseno transformada
arquivo <- read.table("resultados/resultadosRanking/rankingSimCosseno_transformada_angular734.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 4, 5, 36, 2, 12, 22, 25, 26, 39, 8, 10, 34, 6, 19, 28, 32, 35, 38, 3, 7, 9, 11, 13, 14, 15, 17, 18, 21, 23, 24, 29, 30, 33, 20, 27, 31, 16, 37)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 734		", kendall,"		", spearman, "				(1) SIM COSSENO: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Euclidiana original
arquivo <- read.table("resultados/resultadosRanking/rankingEuclidiana_original_angular734.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 4, 5, 36, 2, 12, 22, 25, 26, 39, 8, 10, 34, 6, 19, 28, 32, 35, 38, 3, 7, 9, 11, 13, 14, 15, 17, 18, 21, 23, 24, 29, 30, 33, 20, 27, 31, 16, 37)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 734		", kendall,"		", spearman, "				(1) EUCLIDIANA: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Euclidiana transformada
arquivo <- read.table("resultados/resultadosRanking/rankingEuclidiana_transformada_angular734.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 4, 5, 36, 2, 12, 22, 25, 26, 39, 8, 10, 34, 6, 19, 28, 32, 35, 38, 3, 7, 9, 11, 13, 14, 15, 17, 18, 21, 23, 24, 29, 30, 33, 20, 27, 31, 16, 37)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 734		", kendall,"		", spearman, "				(1) EUCLIDIANA: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#PageRank original
arquivo <- read.table("resultados/resultadosRanking/rankingPageRank_original_angular734.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 4, 5, 36, 2, 12, 22, 25, 26, 39, 8, 10, 34, 6, 19, 28, 32, 35, 38, 3, 7, 9, 11, 13, 14, 15, 17, 18, 21, 23, 24, 29, 30, 33, 20, 27, 31, 16, 37)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 734		", kendall,"		", spearman, "				(2) PAGERANK: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#PageRank transformada
arquivo <- read.table("resultados/resultadosRanking/rankingPageRank_transformada_angular734.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 4, 5, 36, 2, 12, 22, 25, 26, 39, 8, 10, 34, 6, 19, 28, 32, 35, 38, 3, 7, 9, 11, 13, 14, 15, 17, 18, 21, 23, 24, 29, 30, 33, 20, 27, 31, 16, 37)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 734		", kendall,"		", spearman, "				(2) PAGERANK: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Massey original
arquivo <- read.table("resultados/resultadosRanking/rankingMassey_original_angular734.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 4, 5, 36, 2, 12, 22, 25, 26, 39, 8, 10, 34, 6, 19, 28, 32, 35, 38, 3, 7, 9, 11, 13, 14, 15, 17, 18, 21, 23, 24, 29, 30, 33, 20, 27, 31, 16, 37)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 734		", kendall,"		", spearman, "				(2) MASSEY: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Massey transformada
arquivo <- read.table("resultados/resultadosRanking/rankingMassey_transformada_angular734.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 4, 5, 36, 2, 12, 22, 25, 26, 39, 8, 10, 34, 6, 19, 28, 32, 35, 38, 3, 7, 9, 11, 13, 14, 15, 17, 18, 21, 23, 24, 29, 30, 33, 20, 27, 31, 16, 37)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 734		", kendall,"		", spearman, "				(2) MASSEY: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Colley original
arquivo <- read.table("resultados/resultadosRanking/rankingColley_original_angular734.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 4, 5, 36, 2, 12, 22, 25, 26, 39, 8, 10, 34, 6, 19, 28, 32, 35, 38, 3, 7, 9, 11, 13, 14, 15, 17, 18, 21, 23, 24, 29, 30, 33, 20, 27, 31, 16, 37)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 734		", kendall,"		", spearman, "				(2) COLLEY: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Colley original
arquivo <- read.table("resultados/resultadosRanking/rankingColley_transformada_angular734.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 4, 5, 36, 2, 12, 22, 25, 26, 39, 8, 10, 34, 6, 19, 28, 32, 35, 38, 3, 7, 9, 11, 13, 14, 15, 17, 18, 21, 23, 24, 29, 30, 33, 20, 27, 31, 16, 37)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 734		", kendall,"		", spearman, "				(2) COLLEY: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Louvain + PageRank Original
arquivo <- read.table("resultados/resultadosRanking/rankingLouvain+PageRank_original_angular734.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 4, 5, 36, 2, 12, 22, 25, 26, 39, 8, 10, 34, 6, 19, 28, 32, 35, 38, 3, 7, 9, 11, 13, 14, 15, 17, 18, 21, 23, 24, 29, 30, 33, 20, 27, 31, 16, 37)
oraculo <- head(oraculo, numLinhas)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 734		", kendall,"		", spearman, "				(3) LOUVAIN + PAGERANK: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Louvain + PageRank transformada
arquivo <- read.table("resultados/resultadosRanking/rankingLouvain+PageRank_transformada_angular734.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 4, 5, 36, 2, 12, 22, 25, 26, 39, 8, 10, 34, 6, 19, 28, 32, 35, 38, 3, 7, 9, 11, 13, 14, 15, 17, 18, 21, 23, 24, 29, 30, 33, 20, 27, 31, 16, 37)
oraculo <- head(oraculo, numLinhas)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 734		", kendall,"		", spearman, "				(3) LOUVAIN + PAGERANK: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Louvain + Centralidade Original
arquivo <- read.table("resultados/resultadosRanking/rankingLouvain+Centralidade_original_angular734.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 4, 5, 36, 2, 12, 22, 25, 26, 39, 8, 10, 34, 6, 19, 28, 32, 35, 38, 3, 7, 9, 11, 13, 14, 15, 17, 18, 21, 23, 24, 29, 30, 33, 20, 27, 31, 16, 37)
oraculo <- head(oraculo, numLinhas)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 734		", kendall,"		", spearman, "				(3) LOUVAIN + CENTRALIDADE: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Louvain + Centralidade transformada
arquivo <- read.table("resultados/resultadosRanking/rankingLouvain+Centralidade_transformada_angular734.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 4, 5, 36, 2, 12, 22, 25, 26, 39, 8, 10, 34, 6, 19, 28, 32, 35, 38, 3, 7, 9, 11, 13, 14, 15, 17, 18, 21, 23, 24, 29, 30, 33, 20, 27, 31, 16, 37)
oraculo <- head(oraculo, numLinhas)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 734		", kendall,"		", spearman, "				(3) LOUVAIN + CENTRALIDADE: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

test<-("\n\n")
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)


#--------------------------------------------------------------------------------------------------------------------#
#angular_1412

#SimCosseno original
arquivo <- read.table("resultados/resultadosRanking/rankingSimCosseno_original_angular1412.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 3, 4, 7, 15, 29, 6, 10, 12, 14, 16, 18, 22, 23, 24, 28, 30, 31, 5, 26, 33, 2, 8, 19, 20, 21, 9, 11, 13, 17, 25, 27, 32)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 1412		", kendall,"		", spearman, "				(1) SIM COSSENO: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)


#SimCosseno transformada
arquivo <- read.table("resultados/resultadosRanking/rankingSimCosseno_transformada_angular1412.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 3, 4, 7, 15, 29, 6, 10, 12, 14, 16, 18, 22, 23, 24, 28, 30, 31, 5, 26, 33, 2, 8, 19, 20, 21, 9, 11, 13, 17, 25, 27, 32)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 1412		", kendall,"		", spearman, "				(1) SIM COSSENO: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Euclidiana original
arquivo <- read.table("resultados/resultadosRanking/rankingEuclidiana_original_angular1412.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 3, 4, 7, 15, 29, 6, 10, 12, 14, 16, 18, 22, 23, 24, 28, 30, 31, 5, 26, 33, 2, 8, 19, 20, 21, 9, 11, 13, 17, 25, 27, 32)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 1412		", kendall,"		", spearman, "				(1) EUCLIDIANA: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Euclidiana transformada
arquivo <- read.table("resultados/resultadosRanking/rankingEuclidiana_transformada_angular1412.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 3, 4, 7, 15, 29, 6, 10, 12, 14, 16, 18, 22, 23, 24, 28, 30, 31, 5, 26, 33, 2, 8, 19, 20, 21, 9, 11, 13, 17, 25, 27, 32)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 1412		", kendall,"		", spearman, "				(1) EUCLIDIANA: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#PageRank original
arquivo <- read.table("resultados/resultadosRanking/rankingPageRank_original_angular1412.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 3, 4, 7, 15, 29, 6, 10, 12, 14, 16, 18, 22, 23, 24, 28, 30, 31, 5, 26, 33, 2, 8, 19, 20, 21, 9, 11, 13, 17, 25, 27, 32)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 1412		", kendall,"		", spearman, "				(2) PAGERANK: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#PageRank transformada
arquivo <- read.table("resultados/resultadosRanking/rankingPageRank_transformada_angular1412.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 3, 4, 7, 15, 29, 6, 10, 12, 14, 16, 18, 22, 23, 24, 28, 30, 31, 5, 26, 33, 2, 8, 19, 20, 21, 9, 11, 13, 17, 25, 27, 32)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 1412		", kendall,"		", spearman, "				(2) PAGERANK: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Massey original
arquivo <- read.table("resultados/resultadosRanking/rankingMassey_original_angular1412.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 3, 4, 7, 15, 29, 6, 10, 12, 14, 16, 18, 22, 23, 24, 28, 30, 31, 5, 26, 33, 2, 8, 19, 20, 21, 9, 11, 13, 17, 25, 27, 32)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 1412		", kendall,"		", spearman, "				(2) MASSEY: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Massey transformada
arquivo <- read.table("resultados/resultadosRanking/rankingMassey_transformada_angular1412.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 3, 4, 7, 15, 29, 6, 10, 12, 14, 16, 18, 22, 23, 24, 28, 30, 31, 5, 26, 33, 2, 8, 19, 20, 21, 9, 11, 13, 17, 25, 27, 32)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 1412		", kendall,"		", spearman, "				(2) MASSEY: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Colley original
arquivo <- read.table("resultados/resultadosRanking/rankingColley_original_angular1412.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 3, 4, 7, 15, 29, 6, 10, 12, 14, 16, 18, 22, 23, 24, 28, 30, 31, 5, 26, 33, 2, 8, 19, 20, 21, 9, 11, 13, 17, 25, 27, 32)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 1412		", kendall,"		", spearman, "				(2) COLLEY: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Colley original
arquivo <- read.table("resultados/resultadosRanking/rankingColley_transformada_angular1412.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 3, 4, 7, 15, 29, 6, 10, 12, 14, 16, 18, 22, 23, 24, 28, 30, 31, 5, 26, 33, 2, 8, 19, 20, 21, 9, 11, 13, 17, 25, 27, 32)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 1412		", kendall,"		", spearman, "				(2) COLLEY: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Louvain + PageRank Original
arquivo <- read.table("resultados/resultadosRanking/rankingLouvain+PageRank_original_angular1412.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 3, 4, 7, 15, 29, 6, 10, 12, 14, 16, 18, 22, 23, 24, 28, 30, 31, 5, 26, 33, 2, 8, 19, 20, 21, 9, 11, 13, 17, 25, 27, 32)
oraculo <- head(oraculo, numLinhas)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 1412		", kendall,"		", spearman, "				(3) LOUVAIN + PAGERANK: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Louvain + PageRank transformada
arquivo <- read.table("resultados/resultadosRanking/rankingLouvain+PageRank_transformada_angular1412.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 3, 4, 7, 15, 29, 6, 10, 12, 14, 16, 18, 22, 23, 24, 28, 30, 31, 5, 26, 33, 2, 8, 19, 20, 21, 9, 11, 13, 17, 25, 27, 32)
oraculo <- head(oraculo, numLinhas)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 1412		", kendall,"		", spearman, "				(3) LOUVAIN + PAGERANK: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Louvain + Centralidade Original
arquivo <- read.table("resultados/resultadosRanking/rankingLouvain+Centralidade_original_angular1412.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 3, 4, 7, 15, 29, 6, 10, 12, 14, 16, 18, 22, 23, 24, 28, 30, 31, 5, 26, 33, 2, 8, 19, 20, 21, 9, 11, 13, 17, 25, 27, 32)
oraculo <- head(oraculo, numLinhas)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 1412		", kendall,"		", spearman, "				(3) LOUVAIN + CENTRALIDADE: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Louvain + Centralidade transformada
arquivo <- read.table("resultados/resultadosRanking/rankingLouvain+Centralidade_transformada_angular1412.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 3, 4, 7, 15, 29, 6, 10, 12, 14, 16, 18, 22, 23, 24, 28, 30, 31, 5, 26, 33, 2, 8, 19, 20, 21, 9, 11, 13, 17, 25, 27, 32)
oraculo <- head(oraculo, numLinhas)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 1412		", kendall,"		", spearman, "				(3) LOUVAIN + CENTRALIDADE: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

test<-("\n\n")
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#--------------------------------------------------------------------------------------------------------------------#
#angular_583

#SimCosseno original
arquivo <- read.table("resultados/resultadosRanking/rankingSimCosseno_original_angular583.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 2, 8, 10, 11, 13, 18, 7, 12, 3, 4, 5, 6, 9, 14, 16, 17, 26, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 24, 30, 44, 15, 19, 20, 21, 23, 25, 27, 28, 29, 31, 36, 43, 22)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 583		", kendall,"		", spearman, "				(1) SIM COSSENO: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)


#SimCosseno transformada
arquivo <- read.table("resultados/resultadosRanking/rankingSimCosseno_transformada_angular583.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 2, 8, 10, 11, 13, 18, 7, 12, 3, 4, 5, 6, 9, 14, 16, 17, 26, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 24, 30, 44, 15, 19, 20, 21, 23, 25, 27, 28, 29, 31, 36, 43, 22)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 583		", kendall,"		", spearman, "				(1) SIM COSSENO: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Euclidiana original
arquivo <- read.table("resultados/resultadosRanking/rankingEuclidiana_original_angular583.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 2, 8, 10, 11, 13, 18, 7, 12, 3, 4, 5, 6, 9, 14, 16, 17, 26, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 24, 30, 44, 15, 19, 20, 21, 23, 25, 27, 28, 29, 31, 36, 43, 22)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 583		", kendall,"		", spearman, "				(1) EUCLIDIANA: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Euclidiana transformada
arquivo <- read.table("resultados/resultadosRanking/rankingEuclidiana_transformada_angular583.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 2, 8, 10, 11, 13, 18, 7, 12, 3, 4, 5, 6, 9, 14, 16, 17, 26, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 24, 30, 44, 15, 19, 20, 21, 23, 25, 27, 28, 29, 31, 36, 43, 22)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 583		", kendall,"		", spearman, "				(1) EUCLIDIANA: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#PageRank original
arquivo <- read.table("resultados/resultadosRanking/rankingPageRank_original_angular583.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 2, 8, 10, 11, 13, 18, 7, 12, 3, 4, 5, 6, 9, 14, 16, 17, 26, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 24, 30, 44, 15, 19, 20, 21, 23, 25, 27, 28, 29, 31, 36, 43, 22)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 583		", kendall,"		", spearman, "				(2) PAGERANK: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#PageRank transformada
arquivo <- read.table("resultados/resultadosRanking/rankingPageRank_transformada_angular583.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 2, 8, 10, 11, 13, 18, 7, 12, 3, 4, 5, 6, 9, 14, 16, 17, 26, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 24, 30, 44, 15, 19, 20, 21, 23, 25, 27, 28, 29, 31, 36, 43, 22)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 583		", kendall,"		", spearman, "				(2) PAGERANK: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Massey original
arquivo <- read.table("resultados/resultadosRanking/rankingMassey_original_angular583.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 2, 8, 10, 11, 13, 18, 7, 12, 3, 4, 5, 6, 9, 14, 16, 17, 26, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 24, 30, 44, 15, 19, 20, 21, 23, 25, 27, 28, 29, 31, 36, 43, 22)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 583		", kendall,"		", spearman, "				(2) MASSEY: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Massey transformada
arquivo <- read.table("resultados/resultadosRanking/rankingMassey_transformada_angular583.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 2, 8, 10, 11, 13, 18, 7, 12, 3, 4, 5, 6, 9, 14, 16, 17, 26, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 24, 30, 44, 15, 19, 20, 21, 23, 25, 27, 28, 29, 31, 36, 43, 22)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 583		", kendall,"		", spearman, "				(2) MASSEY: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Colley original
arquivo <- read.table("resultados/resultadosRanking/rankingColley_original_angular583.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 2, 8, 10, 11, 13, 18, 7, 12, 3, 4, 5, 6, 9, 14, 16, 17, 26, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 24, 30, 44, 15, 19, 20, 21, 23, 25, 27, 28, 29, 31, 36, 43, 22)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 583		", kendall,"		", spearman, "				(2) COLLEY: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Colley original
arquivo <- read.table("resultados/resultadosRanking/rankingColley_transformada_angular583.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 2, 8, 10, 11, 13, 18, 7, 12, 3, 4, 5, 6, 9, 14, 16, 17, 26, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 24, 30, 44, 15, 19, 20, 21, 23, 25, 27, 28, 29, 31, 36, 43, 22)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 583		", kendall,"		", spearman, "				(2) COLLEY: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Louvain + PageRank Original
arquivo <- read.table("resultados/resultadosRanking/rankingLouvain+PageRank_original_angular583.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 2, 8, 10, 11, 13, 18, 7, 12, 3, 4, 5, 6, 9, 14, 16, 17, 26, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 24, 30, 44, 15, 19, 20, 21, 23, 25, 27, 28, 29, 31, 36, 43, 22)
oraculo <- head(oraculo, numLinhas)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 583		", kendall,"		", spearman, "				(3) LOUVAIN + PAGERANK: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Louvain + PageRank transformada
arquivo <- read.table("resultados/resultadosRanking/rankingLouvain+PageRank_transformada_angular583.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 2, 8, 10, 11, 13, 18, 7, 12, 3, 4, 5, 6, 9, 14, 16, 17, 26, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 24, 30, 44, 15, 19, 20, 21, 23, 25, 27, 28, 29, 31, 36, 43, 22)
oraculo <- head(oraculo, numLinhas)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 583		", kendall,"		", spearman, "				(3) LOUVAIN + PAGERANK: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Louvain + Centralidade Original
arquivo <- read.table("resultados/resultadosRanking/rankingLouvain+Centralidade_original_angular583.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 2, 8, 10, 11, 13, 18, 7, 12, 3, 4, 5, 6, 9, 14, 16, 17, 26, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 24, 30, 44, 15, 19, 20, 21, 23, 25, 27, 28, 29, 31, 36, 43, 22)
oraculo <- head(oraculo, numLinhas)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 583		", kendall,"		", spearman, "				(3) LOUVAIN + CENTRALIDADE: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Louvain + Centralidade transformada
arquivo <- read.table("resultados/resultadosRanking/rankingLouvain+Centralidade_transformada_angular583.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 2, 8, 10, 11, 13, 18, 7, 12, 3, 4, 5, 6, 9, 14, 16, 17, 26, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 24, 30, 44, 15, 19, 20, 21, 23, 25, 27, 28, 29, 31, 36, 43, 22)
oraculo <- head(oraculo, numLinhas)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 583		", kendall,"		", spearman, "				(3) LOUVAIN + CENTRALIDADE: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

test<-("\n\n")
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)


#--------------------------------------------------------------------------------------------------------------------#
#angular_5160


#SimCosseno original
arquivo <- read.table("resultados/resultadosRanking/rankingSimCosseno_original_angular5160.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 5, 6, 2, 3, 7, 9, 14, 15, 4, 8, 10, 12, 13, 16, 21, 24, 11, 17, 18, 19, 20, 22, 23, 25, 26, 27, 28, 29, 30)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 5160		", kendall,"		", spearman, "				(1) SIM COSSENO: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)


#SimCosseno transformada
arquivo <- read.table("resultados/resultadosRanking/rankingSimCosseno_transformada_angular5160.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 5, 6, 2, 3, 7, 9, 14, 15, 4, 8, 10, 12, 13, 16, 21, 24, 11, 17, 18, 19, 20, 22, 23, 25, 26, 27, 28, 29, 30)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 5160		", kendall,"		", spearman, "				(1) SIM COSSENO: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Euclidiana original
arquivo <- read.table("resultados/resultadosRanking/rankingEuclidiana_original_angular5160.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 5, 6, 2, 3, 7, 9, 14, 15, 4, 8, 10, 12, 13, 16, 21, 24, 11, 17, 18, 19, 20, 22, 23, 25, 26, 27, 28, 29, 30)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 5160		", kendall,"		", spearman, "				(1) EUCLIDIANA: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Euclidiana transformada
arquivo <- read.table("resultados/resultadosRanking/rankingEuclidiana_transformada_angular5160.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 5, 6, 2, 3, 7, 9, 14, 15, 4, 8, 10, 12, 13, 16, 21, 24, 11, 17, 18, 19, 20, 22, 23, 25, 26, 27, 28, 29, 30)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 5160		", kendall,"		", spearman, "				(1) EUCLIDIANA: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#PageRank original
arquivo <- read.table("resultados/resultadosRanking/rankingPageRank_original_angular5160.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 5, 6, 2, 3, 7, 9, 14, 15, 4, 8, 10, 12, 13, 16, 21, 24, 11, 17, 18, 19, 20, 22, 23, 25, 26, 27, 28, 29, 30)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 5160		", kendall,"		", spearman, "				(2) PAGERANK: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#PageRank transformada
arquivo <- read.table("resultados/resultadosRanking/rankingPageRank_transformada_angular5160.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 5, 6, 2, 3, 7, 9, 14, 15, 4, 8, 10, 12, 13, 16, 21, 24, 11, 17, 18, 19, 20, 22, 23, 25, 26, 27, 28, 29, 30)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 5160		", kendall,"		", spearman, "				(2) PAGERANK: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Massey original
arquivo <- read.table("resultados/resultadosRanking/rankingMassey_original_angular5160.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 5, 6, 2, 3, 7, 9, 14, 15, 4, 8, 10, 12, 13, 16, 21, 24, 11, 17, 18, 19, 20, 22, 23, 25, 26, 27, 28, 29, 30)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 5160		", kendall,"		", spearman, "				(2) MASSEY: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Massey transformada
arquivo <- read.table("resultados/resultadosRanking/rankingMassey_transformada_angular5160.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 5, 6, 2, 3, 7, 9, 14, 15, 4, 8, 10, 12, 13, 16, 21, 24, 11, 17, 18, 19, 20, 22, 23, 25, 26, 27, 28, 29, 30)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 5160		", kendall,"		", spearman, "				(2) MASSEY: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Colley original
arquivo <- read.table("resultados/resultadosRanking/rankingColley_original_angular5160.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 5, 6, 2, 3, 7, 9, 14, 15, 4, 8, 10, 12, 13, 16, 21, 24, 11, 17, 18, 19, 20, 22, 23, 25, 26, 27, 28, 29, 30)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 5160		", kendall,"		", spearman, "				(2) COLLEY: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Colley original
arquivo <- read.table("resultados/resultadosRanking/rankingColley_transformada_angular5160.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 5, 6, 2, 3, 7, 9, 14, 15, 4, 8, 10, 12, 13, 16, 21, 24, 11, 17, 18, 19, 20, 22, 23, 25, 26, 27, 28, 29, 30)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 5160		", kendall,"		", spearman, "				(2) COLLEY: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Louvain + PageRank Original
arquivo <- read.table("resultados/resultadosRanking/rankingLouvain+PageRank_original_angular5160.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 5, 6, 2, 3, 7, 9, 14, 15, 4, 8, 10, 12, 13, 16, 21, 24, 11, 17, 18, 19, 20, 22, 23, 25, 26, 27, 28, 29, 30)
oraculo <- head(oraculo, numLinhas)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 5160		", kendall,"		", spearman, "				(3) LOUVAIN + PAGERANK: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Louvain + PageRank transformada
arquivo <- read.table("resultados/resultadosRanking/rankingLouvain+PageRank_transformada_angular5160.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 5, 6, 2, 3, 7, 9, 14, 15, 4, 8, 10, 12, 13, 16, 21, 24, 11, 17, 18, 19, 20, 22, 23, 25, 26, 27, 28, 29, 30)
oraculo <- head(oraculo, numLinhas)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 5160		", kendall,"		", spearman, "				(3) LOUVAIN + PAGERANK: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Louvain + Centralidade Original
arquivo <- read.table("resultados/resultadosRanking/rankingLouvain+Centralidade_original_angular5160.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 5, 6, 2, 3, 7, 9, 14, 15, 4, 8, 10, 12, 13, 16, 21, 24, 11, 17, 18, 19, 20, 22, 23, 25, 26, 27, 28, 29, 30)
oraculo <- head(oraculo, numLinhas)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 5160		", kendall,"		", spearman, "				(3) LOUVAIN + CENTRALIDADE: ORIGINAL"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)

#Louvain + Centralidade transformada
arquivo <- read.table("resultados/resultadosRanking/rankingLouvain+Centralidade_transformada_angular5160.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 1:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (0, 1, 5, 6, 2, 3, 7, 9, 14, 15, 4, 8, 10, 12, 13, 16, 21, 24, 11, 17, 18, 19, 20, 22, 23, 25, 26, 27, 28, 29, 30)
oraculo <- head(oraculo, numLinhas)
kendall <- cor(oraculo, rankingAlgoritmo, method="kendall")
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 5160		", kendall,"		", spearman, "				(3) LOUVAIN + CENTRALIDADE: TRANSFORMADA"))
write(test, file="Resultados_kendall_spearman.txt", ncolumns = 5, append=TRUE)
