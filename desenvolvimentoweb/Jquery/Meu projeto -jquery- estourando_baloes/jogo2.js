
timerId = null;

function iniciaJogo(){

	var url = window.location.search;
	
	var nivel_jogo = url.replace("?", "");

	var tempo_segundos = 0;

	if(nivel_jogo == 1) { //1 fácil -> 120segundos
		tempo_segundos = 120;
	}

	if(nivel_jogo == 2) { //2 normal -> 60segundos
		tempo_segundos = 60;
	}
	
	if(nivel_jogo == 3) { //3 difícil -> 30segundos
		tempo_segundos = 30;
	}

	//inserindo segundos no span
	document.getElementById('cronometro').innerHTML = tempo_segundos;

	var quant_baloes = 40;
	cria_baloes(quant_baloes);

	document.getElementById('baloes_inteiros').innerHTML = quant_baloes;
	document.getElementById('baloes_estourados').innerHTML = 0;
	time(tempo_segundos+1)


}

function cria_baloes(qtde_baloes){

	for(var i = 1; i <= qtde_baloes; i++){

		var balao = document.createElement("img");
		balao.src = 'imagens/balao_azul_pequeno.png';
		balao.id = 'b'+i;
		balao.onclick = function(){ estourar(this); };

	

		document.getElementById('cenario').appendChild(balao);

		
	}
}

function estourar(e){
	var id_balao = e.id;
	document.getElementById(id_balao).src = 'imagens/balao_azul_pequeno_estourado.png';

	pontuacao(-1);

}

function time(segundos){
	if(segundos == -1){
	clearTimeout(timerId);
	return false;
	}
	segundos = segundos - 1;

	document.getElementById('cronometro').innerHTML = segundos;
	timerId = setTimeout("time("+segundos+")" , 1000);

}

function pontuacao(acao){
	var baloes_inteiros = document.getElementById('baloes_inteiros').innerHTML;
	var baloes_estourados = document.getElementById('baloes_estourados').innerHTML;

	baloes_inteiros = parseInt(baloes_inteiros);
	baloes_estourados = parseInt(baloes_estourados);

	baloes_inteiros = baloes_inteiros + acao;
	baloes_estourados = baloes_estourados - acao;

	document.getElementById('baloes_inteiros').innerHTML = baloes_inteiros;
	document.getElementById('baloes_estourados').innerHTML = baloes_estourados;


}






