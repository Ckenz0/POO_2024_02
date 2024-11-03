import pytest
from unitario import CadastroUsuario

def test_instanciacao():
    usuario = CadastroUsuario("Maria Souza", "123.456.789-01", "15/04/1988", "Rua B", "(21) 98765-4321", "senha1234")
    assert usuario.nome == "Maria Souza"

def test_validar_nome():
    usuario = CadastroUsuario("Maria Souza", "123.456.789-01", "15/04/1988", "Rua B", "(21) 98765-4321", "senha1234")
    assert usuario.validar_nome() is True

def test_validar_nome_invalido():
    usuario = CadastroUsuario("Maria", "123.456.789-01", "15/04/1988", "Rua B", "(21) 98765-4321", "senha1234")
    with pytest.raises(ValueError):
        usuario.validar_nome()

def test_validar_cpf():
    usuario = CadastroUsuario("Maria Souza", "123.456.789-01", "15/04/1988", "Rua B", "(21) 98765-4321", "senha1234")
    assert usuario.validar_cpf() is True

def test_validar_cpf_invalido():
    usuario = CadastroUsuario("Maria Souza", "12345678901", "15/04/1988", "Rua B", "(21) 98765-4321", "senha1234")
    with pytest.raises(ValueError):
        usuario.validar_cpf()

def test_validar_nascimento():
    usuario = CadastroUsuario("Maria Souza", "123.456.789-01", "15/04/1988", "Rua B", "(21) 98765-4321", "senha1234")
    assert usuario.validar_nascimento() is True

def test_validar_nascimento_invalido():
    usuario = CadastroUsuario("Maria Souza", "123.456.789-01", "32/13/1988", "Rua B", "(21) 98765-4321", "senha1234")
    with pytest.raises(ValueError):
        usuario.validar_nascimento()

def test_validar_telefone():
    usuario = CadastroUsuario("Maria Souza", "123.456.789-01", "15/04/1988", "Rua B", "(21) 98765-4321", "senha1234")
    assert usuario.validar_telefone() is True

def test_validar_telefone_invalido():
    usuario = CadastroUsuario("Maria Souza", "123.456.789-01", "15/04/1988", "Rua B", "98765-4321", "senha1234")
    with pytest.raises(ValueError):
        usuario.validar_telefone()

def test_validar_senha():
    usuario = CadastroUsuario("Maria Souza", "123.456.789-01", "15/04/1988", "Rua B", "(21) 98765-4321", "senha1234")
    assert usuario.validar_senha() is True

def test_validar_senha_invalida():
    usuario = CadastroUsuario("Maria Souza", "123.456.789-01", "15/04/1988", "Rua B", "(21) 98765-4321", "senha")
    with pytest.raises(ValueError):
        usuario.validar_senha()

def test_mostrar_info(capsys):
    usuario = CadastroUsuario("Maria Souza", "123.456.789-01", "15/04/1988", "Rua B", "(21) 98765-4321", "senha1234")
    usuario.mostrar_info()
    captured = capsys.readouterr()
    assert "Maria Souza" in captured.out

def test_gravar_info():
    usuario = CadastroUsuario("Maria Souza", "123.456.789-01", "15/04/1988", "Rua B", "(21) 98765-4321", "senha1234")
    usuario.gravar_info()
    with open("cadastro_123.456.789-01.txt", 'r') as file:
        conteudo = file.read()
        assert "Maria Souza" in conteudo