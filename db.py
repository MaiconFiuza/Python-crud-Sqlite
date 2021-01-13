import sqlite3

#Criação e conexão com o banco
con = sqlite3.connect("dbteste.db")

def criar_tabela_todo():

    cursor = con.cursor()
    con.execute("""
    create table if not exists tarefa(
        cd_tarefa integer primary key autoincrement,
        tarefa text,
        concluido integer
    )
    """)

def add_tarefa(tarefa):
    con.execute("insert into tarefa(tarefa,concluido)values (?,0)",(tarefa,))
    con.commit()

def remove_tarefa(cd_tarefa):
    con.execute("delete from tarefa where cd_tarefa = ?",(cd_tarefa))
    con.commit()

def concluir_tarefa(cd_tarefa):
    con.execute("update tarefa set concluido = 1 where cd_tarefa = ?",(cd_tarefa,))
    con.commit()

def get_tarefas():
    return con.execute("select cd_tarefa, tarefa, concluido from tarefa")