string = "ARQUIVO			 	  SPEARMAN						ESTUDO"
write(string, file="resultados/resultadosMetricas/Resultados_spearman.txt", ncolumns = 5, append=TRUE)
test<-("\n")
write(test, file="resultados/resultadosMetricas/Resultados_spearman.txt", ncolumns = 5, append=TRUE)

#--------------------------------------------------------------------------------------------------------------------#
#angular_2895

#Louvain + Centralidade Original
arquivo <- read.table("resultados/resultadosRanking/rankingLouvain+Centralidade_original_angular2895.txt")
numLinhas <- nrow(arquivo)
if (numLinhas > 10) {
    numLinhas <- 10
}
rankingAlgoritmo <- integer()
for (i in 0:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (17, 13, 18, 20, 23, 27, 28, 33, 10, 2)
oraculo <- head(oraculo, numLinhas)
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 2895		", spearman, "				(3) LOUVAIN + CENTRALIDADE: ORIGINAL"))
write(test, file="resultados/resultadosMetricas/Resultados_spearman.txt", ncolumns = 5, append=TRUE)

#Louvain + Centralidade transformada
arquivo <- read.table("resultados/resultadosRanking/rankingLouvain+Centralidade_transformada_angular2895.txt")
numLinhas <- nrow(arquivo)
if (numLinhas > 10) {
    numLinhas <- 10
}
rankingAlgoritmo <- integer()
for (i in 0:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (17, 13, 18, 20, 23, 27, 28, 33, 10, 2)
oraculo <- head(oraculo, numLinhas)
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 2895		", spearman, "				(3) LOUVAIN + CENTRALIDADE: TRANSFORMADA"))
write(test, file="resultados/resultadosMetricas/Resultados_spearman.txt", ncolumns = 5, append=TRUE)

test<-("\n\n")
write(test, file="resultados/resultadosMetricas/Resultados_spearman.txt", ncolumns = 5, append=TRUE)


#--------------------------------------------------------------------------------------------------------------------#
#angular_734

#Louvain + Centralidade Original
arquivo <- read.table("resultados/resultadosRanking/rankingLouvain+Centralidade_original_angular734.txt")
numLinhas <- nrow(arquivo)
if (numLinhas > 10) {
    numLinhas <- 10
}
rankingAlgoritmo <- integer()
for (i in 0:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (5, 8, 4, 12, 39, 2, 25, 22, 26, 36)
oraculo <- head(oraculo, numLinhas)
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 734		", spearman, "				(3) LOUVAIN + CENTRALIDADE: ORIGINAL"))
write(test, file="resultados/resultadosMetricas/Resultados_spearman.txt", ncolumns = 5, append=TRUE)

#Louvain + Centralidade transformada
arquivo <- tryCatch(read.table("resultados/resultadosRanking/rankingLouvain+Centralidade_transformada_angular734.txt"), error = function(e) NULL)
numLinhas <- nrow(arquivo)
if (numLinhas >= 10) {
    numLinhas <- 10
} 
rankingAlgoritmo <- integer()
for (i in 0:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (5, 8, 4, 12, 39, 2, 25, 22, 26, 36)
oraculo <- head(oraculo, numLinhas)
length(rankingAlgoritmo)
length(oraculo)
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 734		", spearman, "				(3) LOUVAIN + CENTRALIDADE: TRANSFORMADA"))
write(test, file="resultados/resultadosMetricas/Resultados_spearman.txt", ncolumns = 5, append=TRUE)

test<-("\n\n")
write(test, file="resultados/resultadosMetricas/Resultados_spearman.txt", ncolumns = 5, append=TRUE)

#--------------------------------------------------------------------------------------------------------------------#
#angular_1412

#Louvain + Centralidade Original
arquivo <- read.table("resultados/resultadosRanking/rankingLouvain+Centralidade_original_angular1412.txt")
numLinhas <- nrow(arquivo)
if (numLinhas > 10) {
    numLinhas <- 10
}
rankingAlgoritmo <- integer()
for (i in 0:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (6, 15, 24, 29, 12, 4, 3, 16, 10, 7)
oraculo <- head(oraculo, numLinhas)
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 1412		", spearman, "				(3) LOUVAIN + CENTRALIDADE: ORIGINAL"))
write(test, file="resultados/resultadosMetricas/Resultados_spearman.txt", ncolumns = 5, append=TRUE)

#Louvain + Centralidade transformada
arquivo <- read.table("resultados/resultadosRanking/rankingLouvain+Centralidade_transformada_angular1412.txt")
numLinhas <- nrow(arquivo)
if (numLinhas > 10) {
    numLinhas <- 10
}
rankingAlgoritmo <- integer()
for (i in 0:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (6, 15, 24, 29, 12, 4, 3, 16, 10, 7)
oraculo <- head(oraculo, numLinhas)
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 1412		", spearman, "				(3) LOUVAIN + CENTRALIDADE: TRANSFORMADA"))
write(test, file="resultados/resultadosMetricas/Resultados_spearman.txt", ncolumns = 5, append=TRUE)

test<-("\n\n")
write(test, file="resultados/resultadosMetricas/Resultados_spearman.txt", ncolumns = 5, append=TRUE)

#--------------------------------------------------------------------------------------------------------------------#
#angular_583

#Louvain + Centralidade Original
arquivo <- read.table("resultados/resultadosRanking/rankingLouvain+Centralidade_original_angular583.txt")
numLinhas <- nrow(arquivo)
if (numLinhas > 10) {
    numLinhas <- 10
}
rankingAlgoritmo <- integer()   
for (i in 0:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (11, 13, 12, 2, 18, 16, 8, 10, 38, 7)
oraculo <- head(oraculo, numLinhas)
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 583		", spearman, "				(3) LOUVAIN + CENTRALIDADE: ORIGINAL"))
write(test, file="resultados/resultadosMetricas/Resultados_spearman.txt", ncolumns = 5, append=TRUE)

#Louvain + Centralidade transformada
arquivo <- read.table("resultados/resultadosRanking/rankingLouvain+Centralidade_transformada_angular583.txt")
numLinhas <- nrow(arquivo)
if (numLinhas > 10) {
    numLinhas <- 10
}
rankingAlgoritmo <- integer()
for (i in 0:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (11, 13, 12, 2, 18, 16, 8, 10, 38, 7)
oraculo <- head(oraculo, numLinhas)
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 583		", spearman, "				(3) LOUVAIN + CENTRALIDADE: TRANSFORMADA"))
write(test, file="resultados/resultadosMetricas/Resultados_spearman.txt", ncolumns = 5, append=TRUE)

test<-("\n\n")
write(test, file="resultados/resultadosMetricas/Resultados_spearman.txt", ncolumns = 5, append=TRUE)


#--------------------------------------------------------------------------------------------------------------------#
#angular_5160

#Louvain + Centralidade Original
arquivo <- read.table("resultados/resultadosRanking/rankingLouvain+Centralidade_original_angular5160.txt")
numLinhas <- nrow(arquivo)
if (numLinhas > 10) {
    numLinhas <- 10
}
rankingAlgoritmo <- integer()
for (i in 0:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (2, 3, 5, 6, 15, 7, 8, 9, 14, 4)
oraculo <- head(oraculo, numLinhas)
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 5160		", spearman, "				(3) LOUVAIN + CENTRALIDADE: ORIGINAL"))
write(test, file="resultados/resultadosMetricas/Resultados_spearman.txt", ncolumns = 5, append=TRUE)

#Louvain + Centralidade transformada
arquivo <- read.table("resultados/resultadosRanking/rankingLouvain+Centralidade_transformada_angular5160.txt")
numLinhas <- nrow(arquivo)
if (numLinhas > 10) {
    numLinhas <- 10
}
rankingAlgoritmo <- integer()
for (i in 0:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (2, 3, 5, 6, 15, 7, 8, 9, 14, 4)
oraculo <- head(oraculo, numLinhas)
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("ANGULAR 5160		", spearman, "				(3) LOUVAIN + CENTRALIDADE: TRANSFORMADA"))
write(test, file="resultados/resultadosMetricas/Resultados_spearman.txt", ncolumns = 5, append=TRUE)