echo
echo
echo "Executando testes AngularJS..."
echo "Angular_2895.txt"
python main.py -c entradas/angular_2895.txt 0,28,1,17,18,20,23,27,33
echo "Angular_734.txt"
python main.py -c entradas/angular_734.txt 0,1,4,5,36,2,12,22,25,26,39
echo "Angular_1412.txt"
python main.py -c entradas/angular_1412.txt 0,1,3,4,7,15,29
echo "Angular_583.txt"
python main.py -c entradas/angular_583.txt 0,1,2,8,10,11,13,18
echo "Angular_5160.txt"
python main.py -c entradas/angular_5160.txt 0,1,5,6
echo "Fim teste angularjs"
echo
echo

echo "Executando testes jQuery..."
echo "jquery_2145.txt"
python main.py -c entradas/jquery_2145.txt 1,14,2,9,12,13,15,16,17,23,24,26,27,28,33,37
echo "jquery_2310.txt"
python main.py -c entradas/jquery_2310.txt 0,4,30,37,1,5,10,13,14,17,18,19,20,21,25,26,27,31,34,36,38
echo "jquery_2199.txt"
python main.py -c entradas/jquery_2199.txt 0,1,7,9,12,15,16,19,20
echo "jquery_1692.txt"
python main.py -c entradas/jquery_1692.txt 0,1,6,8,10,11,14,17,21,26,28
echo "jquery_2321.txt"
python main.py -c entradas/jquery_2321.txt 0,1,2,17,21
echo "Fim teste jquery"
echo
echo

echo "Executando testes Bootstrap..."
echo "bootstrap_341.txt"
python main.py -c entradas/bootstrap_341.txt 0,1,3,21,29,31,35
echo "bootstrap_1235.txt"
python main.py -c entradas/bootstrap_1235.txt 0,1,2,5,11,18,19,30
echo "bootstrap_931.txt"
python main.py -c entradas/bootstrap_931.txt 0,1,9,13,14,17,21,24,25,26,28,34
echo "bootstrap_1602.txt"
python main.py -c entradas/bootstrap_1602.txt 0,1,4,5,17,20,23,28
echo "bootstrap_1997.txt"
python main.py -c entradas/bootstrap_1997.txt 0,1,2,3
echo "Fim teste"
echo
echo

Rscript spearman_kendall_angular.R
Rscript spearman_kendall_jquery.R
Rscript spearman_kendall_bootstrap.R
