import unittest

from ticTacToe import (askToPlayAgain, boardIsFull, checkWinner, getPlayerMove, playMultipleGames)

class FakeInput:
    def __init__(self, responses):
        self.responses = iter(responses)

    def __call__(self, prompt=""):
        return next(self.responses)

class TestInputValidation(unittest.TestCase):

    def setUp(self):
        self.output = []

    def fakeOutput(self, message=""):
        self.output.append(str(message))

    def testsForNumericalIn(self):
        board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        fakeIn = FakeInput(["hello", "5"])

        result = getPlayerMove(board, "X", input_func=fakeIn, output_func=self.fakeOutput)

        self.assertEqual(result, 4)
        self.assertIn("Please enter a number from 1 to 9.", self.output)

    def testsLessInvalidNumber(self):
        board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        fakeIn = FakeInput(["0", "3"])

        result = getPlayerMove(board, "X", input_func=fakeIn, output_func=self.fakeOutput)

        self.assertEqual(result, 2)
        self.assertIn("Please enter a number from 1 to 9.", self.output)

    def testsGreaterInvalidNumber(self):
        board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        fakeIn = FakeInput(["10", "8"])

        result = getPlayerMove(board, "O", input_func=fakeIn, output_func=self.fakeOutput)

        self.assertEqual(result, 7)
        self.assertIn("Please enter a number from 1 to 9.", self.output)

    def testAlreadyOccupiedPosition(self):
        board = ["X", "2", "3", "4", "5", "6", "7", "8", "9"]
        fakeIn = FakeInput(["1", "2"])

        result = getPlayerMove(board, "O", input_func=fakeIn, output_func=self.fakeOutput)

        self.assertEqual(result, 1)
        self.assertIn("That position has already been chosen.", self.output)

class TestReplayValidation(unittest.TestCase):

    def setUp(self):
        self.output = []

    def fakeOutput(self, message=""):
        self.output.append(str(message))

    def testYes(self):
        fakeIn = FakeInput(["yes"])

        result = askToPlayAgain(input_func=fakeIn, output_func=self.fakeOutput)

        self.assertTrue(result)

    def testUpperYes(self):
        fakeIn = FakeInput(["Y"])

        result = askToPlayAgain(input_func=fakeIn, output_func=self.fakeOutput)

        self.assertTrue(result)

    def testUpperNo(self):
        fakeIn = FakeInput(["n"])

        result = askToPlayAgain(input_func=fakeIn, output_func=self.fakeOutput)

        self.assertFalse(result)

    def testInvalidReply(self):
        fakeIn = FakeInput(["maybe", "y"])

        result = askToPlayAgain(input_func=fakeIn, output_func=self.fakeOutput)
        self.assertTrue(result)
        self.assertIn("Please enter y/yes or n/no.", self.output)

class TestMultipleGames(unittest.TestCase):

    def testMultipleGames(self):
        responses = ["1", "4", "2", "5", "3", "y", "1", "2", "3", "5", "7", "8", "n"]

        fakeIn = FakeInput(responses)
        output = []

        gamesPlayed = playMultipleGames(input_func=fakeIn, output_func=output.append)

        self.assertEqual(gamesPlayed, 2)
        self.assertIn("Player X wins!", output)
        self.assertIn("Player O wins!", output)

    def testOneGame(self):
        responses = ["1", "4", "2", "5", "3", "n"]

        fakeIn = FakeInput(responses)
        output = []

        gamesPlayed = playMultipleGames(input_func=fakeIn, output_func=output.append)

        self.assertEqual(gamesPlayed, 1)

if __name__ == "__main__":
    unittest.main(verbosity=2)