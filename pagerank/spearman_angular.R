string = "ARQUIVO			 	  SPEARMAN						ESTUDO"
write(string, file="resultados/resultadosMetricas/Resultados_spearman.txt", ncolumns = 5, append=TRUE)
test<-("\n")
write(test, file="resultados/resultadosMetricas/Resultados_spearman.txt", ncolumns = 5, append=TRUE)

#--------------------------------------------------------------------------------------------------------------------#
#angular_2895

#PageRank original
arquivo <- read.table("resultados/resultadosRanking/rankingPageRank_original_angular2895.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 0:10)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (17, 13, 18, 20, 23, 27, 28, 33, 10, 2)
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 2895		", spearman, "				(2) PAGERANK: ORIGINAL"))
write(test, file="resultados/resultadosMetricas/Resultados_spearman.txt", ncolumns = 5, append=TRUE)

#PageRank transformada
arquivo <- read.table("resultados/resultadosRanking/rankingPageRank_transformada_angular2895.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 0:10)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (17, 13, 18, 20, 23, 27, 28, 33, 10, 2)
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 2895		", spearman, "				(2) PAGERANK: TRANSFORMADA"))
write(test, file="resultados/resultadosMetricas/Resultados_spearman.txt", ncolumns = 5, append=TRUE)

test<-("\n\n")
write(test, file="resultados/resultadosMetricas/Resultados_spearman.txt", ncolumns = 5, append=TRUE)


#--------------------------------------------------------------------------------------------------------------------#
#angular_734

#PageRank original
arquivo <- read.table("resultados/resultadosRanking/rankingPageRank_original_angular734.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 0:10)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (5, 8, 4, 12, 39, 2, 25, 22, 26, 36)
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 734		", spearman, "				(2) PAGERANK: ORIGINAL"))
write(test, file="resultados/resultadosMetricas/Resultados_spearman.txt", ncolumns = 5, append=TRUE)

#PageRank transformada
arquivo <- read.table("resultados/resultadosRanking/rankingPageRank_transformada_angular734.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 0:10)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (5, 8, 4, 12, 39, 2, 25, 22, 26, 36)
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 734		", spearman, "				(2) PAGERANK: TRANSFORMADA"))
write(test, file="resultados/resultadosMetricas/Resultados_spearman.txt", ncolumns = 5, append=TRUE)

test<-("\n\n")
write(test, file="resultados/resultadosMetricas/Resultados_spearman.txt", ncolumns = 5, append=TRUE)


#--------------------------------------------------------------------------------------------------------------------#
#angular_1412

#PageRank original
arquivo <- read.table("resultados/resultadosRanking/rankingPageRank_original_angular1412.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 0:10)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (6, 15, 24, 29, 12, 4, 3, 16, 10, 7)
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 1412		", spearman, "				(2) PAGERANK: ORIGINAL"))
write(test, file="resultados/resultadosMetricas/Resultados_spearman.txt", ncolumns = 5, append=TRUE)

#PageRank transformada
arquivo <- read.table("resultados/resultadosRanking/rankingPageRank_transformada_angular1412.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 0:10)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (6, 15, 24, 29, 12, 4, 3, 16, 10, 7)
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 1412		", spearman, "				(2) PAGERANK: TRANSFORMADA"))
write(test, file="resultados/resultadosMetricas/Resultados_spearman.txt", ncolumns = 5, append=TRUE)

test<-("\n\n")
write(test, file="resultados/resultadosMetricas/Resultados_spearman.txt", ncolumns = 5, append=TRUE)

#--------------------------------------------------------------------------------------------------------------------#
#angular_583

#PageRank original
arquivo <- read.table("resultados/resultadosRanking/rankingPageRank_original_angular583.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 0:10)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (11, 13, 12, 2, 18, 16, 8, 10, 38, 7)
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 583		", spearman, "				(2) PAGERANK: ORIGINAL"))
write(test, file="resultados/resultadosMetricas/Resultados_spearman.txt", ncolumns = 5, append=TRUE)

#PageRank transformada
arquivo <- read.table("resultados/resultadosRanking/rankingPageRank_transformada_angular583.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 0:10)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (11, 13, 12, 2, 18, 16, 8, 10, 38, 7)
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 583		", spearman, "				(2) PAGERANK: TRANSFORMADA"))
write(test, file="resultados/resultadosMetricas/Resultados_spearman.txt", ncolumns = 5, append=TRUE)

test<-("\n\n")
write(test, file="resultados/resultadosMetricas/Resultados_spearman.txt", ncolumns = 5, append=TRUE)


#--------------------------------------------------------------------------------------------------------------------#
#angular_5160


#PageRank original
arquivo <- read.table("resultados/resultadosRanking/rankingPageRank_original_angular5160.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 0:10)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (2, 3, 5, 6, 15, 7, 8, 9, 14, 4)
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 5160		", spearman, "				(2) PAGERANK: ORIGINAL"))
write(test, file="resultados/resultadosMetricas/Resultados_spearman.txt", ncolumns = 5, append=TRUE)

#PageRank transformada
arquivo <- read.table("resultados/resultadosRanking/rankingPageRank_transformada_angular5160.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 0:10)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (2, 3, 5, 6, 15, 7, 8, 9, 14, 4)
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 5160		", spearman, "				(2) PAGERANK: TRANSFORMADA"))
write(test, file="resultados/resultadosMetricas/Resultados_spearman.txt", ncolumns = 5, append=TRUE)
