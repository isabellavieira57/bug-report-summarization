# Oraculo: top 10 (deve estar ordenado pelos desenvolvedores de 1(mais importante) a 10(menos importante))

echo
echo
echo "Executando testes AngularJS..."
echo "Angular_2895.txt"
python main.py -c entradas/angular_2895.txt 17,13,18,20,23,27,28,33,10,2
echo "Angular_734.txt"
python main.py -c entradas/angular_734.txt 5,8,4,12,39,2,25,22,26,36
echo "Angular_1412.txt"
python main.py -c entradas/angular_1412.txt 6,15,24,29,12,4,3,16,10,7
echo "Angular_583.txt"
python main.py -c entradas/angular_583.txt 11,13,12,2,18,16,8,10,38,7
echo "Angular_5160.txt"
python main.py -c entradas/angular_5160.txt 2,3,5,6,15,7,8,9,14,4
echo "Fim teste angularjs"
echo
echo

echo "Executando testes jQuery..."
echo "jquery_2145.txt"
python main.py -c entradas/jquery_2145.txt 9,2,24,13,16,15,12,14,17,23
echo "jquery_2310.txt"
python main.py -c entradas/jquery_2310.txt 37,5,10,38,30,14,13,4,19,17
echo "jquery_2199.txt"
python main.py -c entradas/jquery_2199.txt 3,7,6,15,20,16,9,12,19,4
echo "jquery_1692.txt"
python main.py -c entradas/jquery_1692.txt 21,11,8,10,14,28,17,6,4,26
echo "jquery_2321.txt"
python main.py -c entradas/jquery_2321.txt 2,3,4,5,17,21,11,10,8,12
echo "Fim teste jquery"
echo
echo

echo "Executando testes Bootstrap..."
echo "bootstrap_341.txt"
python main.py -c entradas/bootstrap_341.txt 30,24,6,9,35,21,31,5,29,3
echo "bootstrap_1235.txt"
python main.py -c entradas/bootstrap_1235.txt 19,18,11,5,22,26,30,2,7,3
echo "bootstrap_931.txt"
python main.py -c entradas/bootstrap_931.txt 28,24,25,26,17,34,14,21,13,9
echo "bootstrap_1602.txt"
python main.py -c entradas/bootstrap_1602.txt 20,3,5,6,4,19,17,23,28,21
echo "bootstrap_1997.txt"
python main.py -c entradas/bootstrap_1997.txt 2,19,3,20,21,23,24,5,22,10
echo "Fim teste"
echo
echo

Rscript spearman_angular.R
Rscript spearman_jquery.R
Rscript spearman_bootstrap.R
