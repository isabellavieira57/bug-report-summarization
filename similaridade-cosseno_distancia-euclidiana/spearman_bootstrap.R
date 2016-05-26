test<-("\n\n")
write(test, file="resultados/resultadosMetricas/Resultados_spearman.txt", ncolumns = 5, append=TRUE)

# bootstrap 341

#SimCosseno original
arquivo <- read.table("resultados/resultadosRanking/rankingSimCosseno_original_bootstrap341.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 0:10)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (30, 24, 6, 9, 35, 21, 31, 5, 29, 3)
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 341		", spearman, "				(1) SIM COSSENO: ORIGINAL"))
write(test, file="resultados/resultadosMetricas/Resultados_spearman.txt", ncolumns = 5, append=TRUE)

#SimCosseno transformada
arquivo <- read.table("resultados/resultadosRanking/rankingSimCosseno_transformada_bootstrap341.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 0:10)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (30, 24, 6, 9, 35, 21, 31, 5, 29, 3)
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 341		", spearman, "				(1) SIM COSSENO: TRANSFORMADA"))
write(test, file="resultados/resultadosMetricas/Resultados_spearman.txt", ncolumns = 5, append=TRUE)

#Euclidiana original
arquivo <- read.table("resultados/resultadosRanking/rankingEuclidiana_original_bootstrap341.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 0:10)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (30, 24, 6, 9, 35, 21, 31, 5, 29, 3)
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 341		", spearman, "				(1) EUCLIDIANA: ORIGINAL"))
write(test, file="resultados/resultadosMetricas/Resultados_spearman.txt", ncolumns = 5, append=TRUE)

#Euclidiana transformada
arquivo <- read.table("resultados/resultadosRanking/rankingEuclidiana_transformada_bootstrap341.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 0:10)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (30, 24, 6, 9, 35, 21, 31, 5, 29, 3)
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 341		", spearman, "				(1) EUCLIDIANA: TRANSFORMADA"))
write(test, file="resultados/resultadosMetricas/Resultados_spearman.txt", ncolumns = 5, append=TRUE)

test<-("\n\n")
write(test, file="resultados/resultadosMetricas/Resultados_spearman.txt", ncolumns = 5, append=TRUE)

#----------------------------------------------------------------------------------------#
#bootstrap 1235

#SimCosseno original
arquivo <- read.table("resultados/resultadosRanking/rankingSimCosseno_original_bootstrap1235.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 0:10)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (19, 18, 11, 5, 22, 26, 30, 2, 7, 3)
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 1235		", spearman, "				(1) SIM COSSENO: ORIGINAL"))
write(test, file="resultados/resultadosMetricas/Resultados_spearman.txt", ncolumns = 5, append=TRUE)

#SimCosseno transformada
arquivo <- read.table("resultados/resultadosRanking/rankingSimCosseno_transformada_bootstrap1235.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 0:10)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (19, 18, 11, 5, 22, 26, 30, 2, 7, 3)
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 1235		", spearman, "				(1) SIM COSSENO: TRANSFORMADA"))
write(test, file="resultados/resultadosMetricas/Resultados_spearman.txt", ncolumns = 5, append=TRUE)

#Euclidiana original
arquivo <- read.table("resultados/resultadosRanking/rankingEuclidiana_original_bootstrap1235.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 0:10)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (19, 18, 11, 5, 22, 26, 30, 2, 7, 3)
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 1235		", spearman, "				(1) EUCLIDIANA: ORIGINAL"))
write(test, file="resultados/resultadosMetricas/Resultados_spearman.txt", ncolumns = 5, append=TRUE)

#Euclidiana transformada
arquivo <- read.table("resultados/resultadosRanking/rankingEuclidiana_transformada_bootstrap1235.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 0:10)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (19, 18, 11, 5, 22, 26, 30, 2, 7, 3)
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 1235		", spearman, "				(1) EUCLIDIANA: TRANSFORMADA"))
write(test, file="resultados/resultadosMetricas/Resultados_spearman.txt", ncolumns = 5, append=TRUE)

test<-("\n\n")
write(test, file="resultados/resultadosMetricas/Resultados_spearman.txt", ncolumns = 5, append=TRUE)

#----------------------------------------------------------------------------------------#
#bootstrap 931

#SimCosseno original
arquivo <- read.table("resultados/resultadosRanking/rankingSimCosseno_original_bootstrap931.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 0:10)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (28, 24, 25, 26, 17, 34, 14, 21, 13, 9)
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 931		", spearman, "				(1) SIM COSSENO: ORIGINAL"))
write(test, file="resultados/resultadosMetricas/Resultados_spearman.txt", ncolumns = 5, append=TRUE)

#SimCosseno transformada
arquivo <- read.table("resultados/resultadosRanking/rankingSimCosseno_transformada_bootstrap931.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 0:10)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (28, 24, 25, 26, 17, 34, 14, 21, 13, 9)
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 931		", spearman, "				(1) SIM COSSENO: TRANSFORMADA"))
write(test, file="resultados/resultadosMetricas/Resultados_spearman.txt", ncolumns = 5, append=TRUE)

#Euclidiana original
arquivo <- read.table("resultados/resultadosRanking/rankingEuclidiana_original_bootstrap931.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 0:10)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (28, 24, 25, 26, 17, 34, 14, 21, 13, 9)
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 931		", spearman, "				(1) EUCLIDIANA: ORIGINAL"))
write(test, file="resultados/resultadosMetricas/Resultados_spearman.txt", ncolumns = 5, append=TRUE)

#Euclidiana transformada
arquivo <- read.table("resultados/resultadosRanking/rankingEuclidiana_transformada_bootstrap931.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 0:10)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (28, 24, 25, 26, 17, 34, 14, 21, 13, 9)
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 931		", spearman, "				(1) EUCLIDIANA: TRANSFORMADA"))
write(test, file="resultados/resultadosMetricas/Resultados_spearman.txt", ncolumns = 5, append=TRUE)

test<-("\n\n")
write(test, file="resultados/resultadosMetricas/Resultados_spearman.txt", ncolumns = 5, append=TRUE)

#----------------------------------------------------------------------------------------#
#bootstrap 1602

#SimCosseno original
arquivo <- read.table("resultados/resultadosRanking/rankingSimCosseno_original_bootstrap1602.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 0:10)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (20, 3, 5, 6, 4, 19, 17, 23, 28, 21)
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 1602		", spearman, "				(1) SIM COSSENO: ORIGINAL"))
write(test, file="resultados/resultadosMetricas/Resultados_spearman.txt", ncolumns = 5, append=TRUE)

#SimCosseno transformada
arquivo <- read.table("resultados/resultadosRanking/rankingSimCosseno_transformada_bootstrap1602.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 0:10)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (20, 3, 5, 6, 4, 19, 17, 23, 28, 21)
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 1602		", spearman, "				(1) SIM COSSENO: TRANSFORMADA"))
write(test, file="resultados/resultadosMetricas/Resultados_spearman.txt", ncolumns = 5, append=TRUE)

#Euclidiana original
arquivo <- read.table("resultados/resultadosRanking/rankingEuclidiana_original_bootstrap1602.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 0:10)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (20, 3, 5, 6, 4, 19, 17, 23, 28, 21)
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 1602		", spearman, "				(1) EUCLIDIANA: ORIGINAL"))
write(test, file="resultados/resultadosMetricas/Resultados_spearman.txt", ncolumns = 5, append=TRUE)

#Euclidiana transformada
arquivo <- read.table("resultados/resultadosRanking/rankingEuclidiana_transformada_bootstrap1602.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 0:10)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (20, 3, 5, 6, 4, 19, 17, 23, 28, 21)
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 1602		", spearman, "				(1) EUCLIDIANA: TRANSFORMADA"))
write(test, file="resultados/resultadosMetricas/Resultados_spearman.txt", ncolumns = 5, append=TRUE)

test<-("\n\n")
write(test, file="resultados/resultadosMetricas/Resultados_spearman.txt", ncolumns = 5, append=TRUE)

#----------------------------------------------------------------------------------------#
#bootstrap 1997

#SimCosseno original
arquivo <- read.table("resultados/resultadosRanking/rankingSimCosseno_original_bootstrap1997.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 0:10)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (2, 19, 3, 20, 21, 23, 24, 5, 22, 10)
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 1997		", spearman, "				(1) SIM COSSENO: ORIGINAL"))
write(test, file="resultados/resultadosMetricas/Resultados_spearman.txt", ncolumns = 5, append=TRUE)

#SimCosseno transformada
arquivo <- read.table("resultados/resultadosRanking/rankingSimCosseno_transformada_bootstrap1997.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 0:10)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (2, 19, 3, 20, 21, 23, 24, 5, 22, 10)
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 1997		", spearman, "				(1) SIM COSSENO: TRANSFORMADA"))
write(test, file="resultados/resultadosMetricas/Resultados_spearman.txt", ncolumns = 5, append=TRUE)

#Euclidiana original
arquivo <- read.table("resultados/resultadosRanking/rankingEuclidiana_original_bootstrap1997.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 0:10)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (2, 19, 3, 20, 21, 23, 24, 5, 22, 10)
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 1997		", spearman, "				(1) EUCLIDIANA: ORIGINAL"))
write(test, file="resultados/resultadosMetricas/Resultados_spearman.txt", ncolumns = 5, append=TRUE)

#Euclidiana transformada
arquivo <- read.table("resultados/resultadosRanking/rankingEuclidiana_transformada_bootstrap1997.txt")
numLinhas <- nrow(arquivo)
rankingAlgoritmo <- integer()
for (i in 0:10)	rankingAlgoritmo[i] <- arquivo[i,]
oraculo <- c (2, 19, 3, 20, 21, 23, 24, 5, 22, 10)
spearman <- cor(oraculo, rankingAlgoritmo, method="spearman")
test<-t(rbind("BOOTSTAP 1997		", spearman, "				(1) EUCLIDIANA: TRANSFORMADA"))
write(test, file="resultados/resultadosMetricas/Resultados_spearman.txt", ncolumns = 5, append=TRUE)

test<-("\n\n")
write(test, file="resultados/resultadosMetricas/Resultados_spearman.txt", ncolumns = 5, append=TRUE)