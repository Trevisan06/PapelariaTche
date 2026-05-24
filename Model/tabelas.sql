create table clientes (
cpf bigint(11) primary Key,
nome varchar (150) not null,
dataNascimento date not null,
pontos int not null,
contato bigint(11) not null,
email text not null,
parcelas int not null
);




create table parcelas (
codParcelas int primary key auto_increment,
codVenda int auto_increment primary key,
numeroParcela int not null,
valorParcela double not null,
dataVencimento date not null,
dataPagamento date not null,
statusParcela text not null, 
)

create table produtos (
codProduto int primary key auto_increment,
nome varchar(60) not null,
categoria varchar (100) not null,
preco double not null
quantidadeEstoque int not null,
marca varchar(45),
validade date not null,
)


create table compra (
idCompra int primary key auto_increment,
dataCompra date not null,
valorCompra double not null,
codFornecedor int auto_increment,
formaPagamento varchar(20),
quantidadeItens int not null,
)

create table saldoPontos (
idPontos int 
idclientes int
saldoAtual int
pontosGanhos int
pontosUsados int
dataDaUltimaMovimentacao date 
statusDaconta varchar (150)
)

create table funcionario (
idFuncionarios int primary key not null,
nome varchar(45) not null
cargo varchar(60) not null,
salario double not null,
telefone bigint(11),
matricula int not null,
metaDeVendas text not null,
)


create table promocao (
codPromocao int primary key auto_increment
nome varchar(45) not null,
desconto int not null,
dataInicio date not null,
dataFim date not null,
motivo text,
codProdutos int primary key,
)

create table pedidoOnline (
id int auto_increment primary key,
dataPedido date 
valorPedido decimal (10,2)
formaEntrega varchar (150) 
statusEntrega varchar (150)
enderecoEntrega varchar (150)

create table categoria (
id int auto_increment primary key,
nomeCategoria varchar (150)
descricao Varchar (150)
setor Varchar (150)
fileira int 
relevancia varchar (150)
)

create table filial (
    id int primary key auto_increment,
    nomeFilial varchar(100) not null,
    cidade varchar(100) not null,
    estado varchar(100) not null,
    endereco varchar(150) not null,
    telefone bigint(11) not null,
    gerente varchar(100) not null,
    quantidadeFuncionarios int not null,
    horarioFuncionamento varchar(100) not null,
    email varchar(150)