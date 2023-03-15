import sys
from io import TextIOWrapper

import click

# from config import Config
# import config
from config import Config

config = Config()


@click.command()
@click.argument("input", type=click.File("r"), default=sys.stdin)
@click.argument("output", type=click.File("w"), default=sys.stdout)
@click.option("--tabsize", type=int, default=4)
def cli(input: TextIOWrapper, output: TextIOWrapper, tabsize: int):
    from surreal_formatter import parse

    config.tabsize = tabsize
    text = input.read()
    text = parse(text)
    text = text.expandtabs(tabsize)
    output.write(text)


# if __name__ == "__main__":
# main()
#     text = """
# # comment
# -- comment
# // comment
# /* comment */
# /*
# comment
# */
# /*
#
# comment
#
# */
#
# DEFINE TABLE user SCHEMAFULL;
# DEFINE TABLE user SCHEMALESS PERMISSIONS FOR select, create, update, delete NONE;
# DEFINE TABLE user SCHEMALESS PERMISSIONS NONE;
# DEFINE TABLE user SCHEMALESS PERMISSIONS FOR select WHERE id = $auth.id OR admin = true, FOR create, update, delete NONE;
# # fields
# DEFINE FIELD creditors ON user TYPE array;
# SELECT * FROM user;
# SELECT * FROM account;
# """
#     text = """
# DEFINE TABLE creditor SCHEMALESS PERMISSIONS FOR select WHERE $auth.creditors ?= id, FOR create NONE, FOR update NONE, FOR delete NONE;
# DEFINE TABLE member SCHEMALESS PERMISSIONS FOR select WHERE id = $auth.id, FOR create FULL, FOR update FULL, FOR delete FULL;
# DEFINE TABLE member_signup SCHEMALESS PERMISSIONS NONE;
# DEFINE TABLE packaging SCHEMALESS PERMISSIONS NONE;
# DEFINE TABLE product SCHEMALESS PERMISSIONS FOR select WHERE $auth.creditors ?= creditor, FOR create NONE, FOR update NONE, FOR delete NONE;
# DEFINE TABLE provide SCHEMALESS PERMISSIONS FOR select WHERE $auth.creditors ?= in, FOR create NONE, FOR update NONE, FOR delete NONE;
# DEFINE TABLE user SCHEMALESS PERMISSIONS FOR select WHERE id = $auth.id, FOR create NONE, FOR update NONE, FOR delete NONE;
# DEFINE TABLE user_signup SCHEMALESS PERMISSIONS NONE;
# DEFINE FIELD creditors ON user TYPE array;
# DEFINE FIELD creditors[*] ON user TYPE record(creditor) ASSERT $value.id != NONE;
# DEFINE FIELD pass ON user TYPE string PERMISSIONS FOR select NONE, FOR create FULL, FOR update WHERE id = $auth.id, FOR delete FULL;
# DEFINE TABLE provide SCHEMALESS PERMISSIONS FOR select WHERE $auth.creditors ?= in FOR create, update, delete NONE;
# SELECT * FROM user;
# SELECT name, email FROM user WHERE email = 'leander.hofmann@troiber.de';
# """
# result = formatter.parse(text)
# print(formatter.parse(text))
