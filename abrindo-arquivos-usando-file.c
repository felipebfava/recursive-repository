#include <stdio.h>
#include <stdlib.h>

int main()  {
		
	int vetor[6]; //cria um vetor para receber o tamanho que tem dentro do arquivo
	int i; //para itera��o do for
	
	FILE *arquivo; //cria um arquivo
	arquivo = fopen("C:\\Users\\User\\OneDrive\\�rea de Trabalho\\teste.txt", "r"); //abre o arquivo usando duas contrabarras para leitura
		
	//utiliza for para caminhar sobre cada caracter do arquivo para escrever no vetor
	for(i = 0; i < 6; i++)
		fscanf(arquivo, "%d\n", &vetor[i]);
	
	arquivo = fopen("teste02.txt", "w"); //nesse caso, como n�o existia teste02, a fun�ao cria ele e habilita para escrever dentro
	
	//utiliza for para escrever no arquivo, por�m o novo arquivo ter� somado cada n�mero +2
	for(i=0; i<6; i++)
		fprintf(arquivo, "%d\n", vetor[i]+2);
	
	fclose(arquivo); //para fechar o arquivo
}
