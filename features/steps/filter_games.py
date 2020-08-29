from behave import *
from src.Game import *
from src.Catalogue import *

#Condiciones antes de empezar cualquier STEP
def before_scenario(context, scenario):
	context = {}

@given("a set of games")
def step_impl(context):
	game_list = []

	for row in context.table:

		elenco = []
		idiomas = []
		game = Game(row['NAME'], row['RELEASE DATE'], row['DEVELOPER'], row['RATE'])
		game_list.append(game)

	context.games = game_list

@given('the user enters the name: {name}')
def step_impl(context, name):
	context.name = name


@when("the user search games by {criteria}")
def step_impl(context, criteria):
	if(criteria == 'name'):
		result, message = get_game_name(context.games, context.name)
		print(result)
		context.result = result
		context.message = message


@then("{total} games will match")
def step_impl(context, total):
	assert len(context.result) == int(total)


@then("the names of these games are")
def step_impl(context):
	expected_games = True
	result_games = []
	for row in context.table:
		result_games.append(row['NAME'])
	for game in context.result:
		if game.name not in result_games:
			print("No game " + game.name)
			expected_games = False
	assert expected_games is True

@then("the following message is displayed: {message}")
def step_impl(context, message):
	print(message)
	print(context.message)
	assert context.message == message

	@given("the user selects one or more ratings: {rating}")
def step_impl(context, rating):
	context.rating = rating.split(",")

@when("choosing the search by ratings {option}")
def step_impl(context, option):
	if(option == "name"):
		r, message = get_game_name(context.games, context.name)
		print(r)
		context.r=r
		context.message=message
	elif(option == "rating"):
		r,message, err=get_game_rating(context.games, context.rating)
		print(r)
		context.r=r
		context.message=message

@then("the name of all the games that correspond to these categories will be displayed: {message}")
def step_impl(context, message):
	print(message)
	print(context.message)
	assert context.message == message
"""
@given("the user selects one or more ratings: {rating1}")
def step_impl(context, rating1):
	context.rating = rating1.split(",")

@when("choosing the no match ratings {option1}")
def step_impl(context, option1):
	if(option1 == "name"):
		r, message = get_game_name(context.games, context.name)
		print(r)
		context.r=r
		context.message=message
	elif(option1 == "rating"):
		r,message, err=get_game_rating(context.games, context.rating)
		print(r)
		context.r=r
		context.message=message"""

@then("No game with the specified rating was found: {message}")
def step_impl(context, message):
	print(message)
	print(context.message)
	assert context.message == message


@given("the user enters a studio: {studio}")
def step_impl(context, studio):
	context.rating = studio

@when("they select the search by studio {option}")
def step_impl(context, option):
	if(option == "name"):
		r, message = get_game_name(context.games, context.name)
		print(r)
		context.r=r
		context.message=message
	elif(option == "rating"):
		r,message, err=get_game_rating(context.games, context.rating)
		print(r)
		context.r=r
		context.message=message

@then("the name of all the games that have been developed by that studio will be displayed: {message}")
def step_impl(context, message):
	print(message)
	print(context.message)
	assert context.message == message

