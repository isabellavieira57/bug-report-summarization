test<-("\n\n")
write(test, file="resultados/resultadosMetricas/Resultados_spearman.txt", ncolumns = 5, append=TRUE)

# jquery 2145

#Louvain + Centralidade Original
arquivo <- read.table("resultados/resultadosRanking/rankingLouvain+Centralidade_original_jquery2145.txt")
numLinhas <- nrow(arquivo)
if (numLinhas > 10) {
    numLinhas <- 10
}
rankingAlgoritmo <- integer()
for (i in 0:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (9, 2, 24, 13, 16, 15, 12, 14, 17, 23)
oraculo <- head(oraculo, numLinhas)
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("JQUERY 2145		", spearman, "				(3) LOUVAIN + CENTRALIDADE: ORIGINAL"))
write(test, file="resultados/resultadosMetricas/Resultados_spearman.txt", ncolumns = 5, append=TRUE)

#Louvain + Centralidade transformada
arquivo <- read.table("resultados/resultadosRanking/rankingLouvain+Centralidade_transformada_jquery2145.txt")
numLinhas <- nrow(arquivo)
if (numLinhas > 10) {
    numLinhas <- 10
}
rankingAlgoritmo <- integer()
for (i in 0:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (9, 2, 24, 13, 16, 15, 12, 14, 17, 23)
oraculo <- head(oraculo, numLinhas)
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("JQUERY 2145		", spearman, "				(3) LOUVAIN + CENTRALIDADE: TRANSFORMADA"))
write(test, file="resultados/resultadosMetricas/Resultados_spearman.txt", ncolumns = 5, append=TRUE)

test<-("\n\n")
write(test, file="resultados/resultadosMetricas/Resultados_spearman.txt", ncolumns = 5, append=TRUE)

#----------------------------------------------------------------------------------------#
# jquery 2310

#Louvain + Centralidade Original
arquivo <- read.table("resultados/resultadosRanking/rankingLouvain+Centralidade_original_jquery2310.txt")
numLinhas <- nrow(arquivo)
if (numLinhas > 10) {
    numLinhas <- 10
}
rankingAlgoritmo <- integer()
for (i in 0:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (37, 5, 10, 38, 30, 14, 13, 4, 19, 17)
oraculo <- head(oraculo, numLinhas)
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("JQUERY 2310		", spearman, "				(3) LOUVAIN + CENTRALIDADE: ORIGINAL"))
write(test, file="resultados/resultadosMetricas/Resultados_spearman.txt", ncolumns = 5, append=TRUE)

#Louvain + Centralidade transformada
arquivo <- read.table("resultados/resultadosRanking/rankingLouvain+Centralidade_transformada_jquery2310.txt")
numLinhas <- nrow(arquivo)
if (numLinhas > 10) {
    numLinhas <- 10
}
rankingAlgoritmo <- integer()
for (i in 0:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (37, 5, 10, 38, 30, 14, 13, 4, 19, 17)
oraculo <- head(oraculo, numLinhas)
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("JQUERY 2310		", spearman, "				(3) LOUVAIN + CENTRALIDADE: TRANSFORMADA"))
write(test, file="resultados/resultadosMetricas/Resultados_spearman.txt", ncolumns = 5, append=TRUE)

test<-("\n\n")
write(test, file="resultados/resultadosMetricas/Resultados_spearman.txt", ncolumns = 5, append=TRUE)

#----------------------------------------------------------------------------------------#
# jquery 2199

#Louvain + Centralidade Original
arquivo <- read.table("resultados/resultadosRanking/rankingLouvain+Centralidade_original_jquery2199.txt")
numLinhas <- nrow(arquivo)
if (numLinhas > 10) {
    numLinhas <- 10
}
rankingAlgoritmo <- integer()
for (i in 0:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (3, 7, 6, 15, 20, 16, 9, 12, 19, 4)
oraculo <- head(oraculo, numLinhas)
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("JQUERY 2199		", spearman, "				(3) LOUVAIN + CENTRALIDADE: ORIGINAL"))
write(test, file="resultados/resultadosMetricas/Resultados_spearman.txt", ncolumns = 5, append=TRUE)

#Louvain + Centralidade transformada
arquivo <- read.table("resultados/resultadosRanking/rankingLouvain+Centralidade_transformada_jquery2199.txt")
numLinhas <- nrow(arquivo)
if (numLinhas > 10) {
    numLinhas <- 10
}
rankingAlgoritmo <- integer()
for (i in 0:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (3, 7, 6, 15, 20, 16, 9, 12, 19, 4)
oraculo <- head(oraculo, numLinhas)
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("JQUERY 2199		", spearman, "				(3) LOUVAIN + CENTRALIDADE: TRANSFORMADA"))
write(test, file="resultados/resultadosMetricas/Resultados_spearman.txt", ncolumns = 5, append=TRUE)

test<-("\n\n")
write(test, file="resultados/resultadosMetricas/Resultados_spearman.txt", ncolumns = 5, append=TRUE)

#----------------------------------------------------------------------------------------#
# jquery 2321

#Louvain + Centralidade Original
arquivo <- read.table("resultados/resultadosRanking/rankingLouvain+Centralidade_original_jquery2321.txt")
numLinhas <- nrow(arquivo)
if (numLinhas > 10) {
    numLinhas <- 10
}
rankingAlgoritmo <- integer()
for (i in 0:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (2, 3, 4, 5, 17, 21, 11, 10, 8, 12)
oraculo <- head(oraculo, numLinhas)
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("JQUERY 2321		", spearman, "				(3) LOUVAIN + CENTRALIDADE: ORIGINAL"))
write(test, file="resultados/resultadosMetricas/Resultados_spearman.txt", ncolumns = 5, append=TRUE)

#Louvain + Centralidade transformada
arquivo <- read.table("resultados/resultadosRanking/rankingLouvain+Centralidade_transformada_jquery2321.txt")
numLinhas <- nrow(arquivo)
if (numLinhas > 10) {
    numLinhas <- 10
}
rankingAlgoritmo <- integer()
for (i in 0:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (2, 3, 4, 5, 17, 21, 11, 10, 8, 12)
oraculo <- head(oraculo, numLinhas)
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("JQUERY 2321		", spearman, "				(3) LOUVAIN + CENTRALIDADE: TRANSFORMADA"))
write(test, file="resultados/resultadosMetricas/Resultados_spearman.txt", ncolumns = 5, append=TRUE)

test<-("\n\n")
write(test, file="resultados/resultadosMetricas/Resultados_spearman.txt", ncolumns = 5, append=TRUE)

#----------------------------------------------------------------------------------------#

#jquery 1692

#Louvain + Centralidade Original
arquivo <- read.table("resultados/resultadosRanking/rankingLouvain+Centralidade_original_jquery1692.txt")
numLinhas <- nrow(arquivo)
if (numLinhas > 10) {
    numLinhas <- 10
}
rankingAlgoritmo <- integer()
for (i in 0:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (21, 11, 8, 10, 14, 28, 17, 6, 4, 26)
oraculo <- head(oraculo, numLinhas)
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("JQUERY 1692		", spearman, "				(3) LOUVAIN + CENTRALIDADE: ORIGINAL"))
write(test, file="resultados/resultadosMetricas/Resultados_spearman.txt", ncolumns = 5, append=TRUE)

#Louvain + Centralidade transformada
arquivo <- read.table("resultados/resultadosRanking/rankingLouvain+Centralidade_transformada_jquery1692.txt")
numLinhas <- nrow(arquivo)
if (numLinhas > 10) {
    numLinhas <- 10
}
rankingAlgoritmo <- integer()
for (i in 0:numLinhas)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (21, 11, 8, 10, 14, 28, 17, 6, 4, 26)
oraculo <- head(oraculo, numLinhas)
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("JQUERY 1692		", spearman, "				(3) LOUVAIN + CENTRALIDADE: TRANSFORMADA"))
write(test, file="resultados/resultadosMetricas/Resultados_spearman.txt", ncolumns = 5, append=TRUE)

test<-("\n\n")
write(test, file="resultados/resultadosMetricas/Resultados_spearman.txt", ncolumns = 5, append=TRUE)
