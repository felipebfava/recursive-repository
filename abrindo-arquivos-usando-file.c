#include <stdio.h>
#include <stdlib.h>

int main()  {
		
	int vetor[6]; //cria um vetor para receber o tamanho que tem dentro do arquivo
	int i; //para iteração do for
	
	FILE *arquivo; //cria um arquivo
	arquivo = fopen("C:\\Users\\User\\OneDrive\\Área de Trabalho\\teste.txt", "r"); //abre o arquivo usando duas contrabarras para leitura
		
	//utiliza for para caminhar sobre cada caracter do arquivo para escrever no vetor
	for(i = 0; i < 6; i++)
		fscanf(arquivo, "%d\n", &vetor[i]);
	
	arquivo = fopen("teste02.txt", "w"); //nesse caso, como não existia teste02, a funçao cria ele e habilita para escrever dentro
	
	//utiliza for para escrever no arquivo, porém o novo arquivo terá somado cada número +2
	for(i=0; i<6; i++)
		fprintf(arquivo, "%d\n", vetor[i]+2);
	
	fclose(arquivo); //para fechar o arquivo
}
