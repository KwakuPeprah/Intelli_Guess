import unittest
from unittest.mock import patch #patch lets you simulate user input by temporarily replacing the input function

# IMPORTANT: Ensure your game logic file is imported and aliased as 'game'.
import intelli_guess as game 

class TestIntelliGuess(unittest.TestCase):
    """Unit tests for the IntelliGuess project."""

    # -------------------------------
    # Difficulty Level Tests
    # -------------------------------
    def test_difficulty_levels_setup(self):
        """Check if difficulty levels dictionary is correctly defined (Name, Min, Max)."""
        self.assertIn('1', game.DIFFICULTY_LEVELS)
        self.assertEqual(game.DIFFICULTY_LEVELS['1'], ('Easy', 1, 10))
        self.assertEqual(game.DIFFICULTY_LEVELS['2'], ('Medium', 1, 100))
        self.assertEqual(game.DIFFICULTY_LEVELS['3'], ('Hard', 1, 1000))

    @patch('builtins.input', side_effect=['2']) #builtins specifies the function to be replaced. In this case, the input function. side_effect tells the replacement function what to return
    def test_select_difficulty_returns_expected_range(self, mock_input):
        """Test selecting difficulty returns correct (Name, Min, Max) tuple."""
        result = game.select_difficulty()
        self.assertEqual(result, ('Medium', 1, 100))
        
    @patch('builtins.input', side_effect=['4', 'abc', '1'])
    def test_select_difficulty_invalid_then_valid(self, mock_input):
        """Test handling of invalid difficulty choices followed by a valid choice."""
        result = game.select_difficulty()
        self.assertEqual(result, ('Easy', 1, 10))

    # -------------------------------
    # Guess Input Tests
    # -------------------------------
    @patch('builtins.input', side_effect=['5'])
    def test_get_valid_guess_valid(self, mock_input):
        """Test valid integer guess within range."""
        result = game.get_valid_guess(1, 10)
        self.assertEqual(result, 5)

    @patch('builtins.input', side_effect=['abc', '15', '7'])
    def test_get_valid_guess_invalid_then_valid(self, mock_input):
        """Test invalid inputs (non-numeric, out-of-range) followed by a valid guess."""
        result = game.get_valid_guess(1, 10)
        self.assertEqual(result, 7)

    @patch('builtins.input', side_effect=['exit'])
    def test_get_valid_guess_exit(self, mock_input):
        """Test typing 'exit' to quit."""
        result = game.get_valid_guess(1, 10)
        self.assertEqual(result, 'exit')

    # -------------------------------
    # Play Again Tests
    # -------------------------------
    @patch('builtins.input', side_effect=['y'])
    def test_play_again_yes(self, mock_input):
        """Test 'y' input returns True."""
        self.assertTrue(game.play_again())

    @patch('builtins.input', side_effect=['n'])
    def test_play_again_no(self, mock_input):
        """Test 'n' input returns False."""
        self.assertFalse(game.play_again())

    @patch('builtins.input', side_effect=['invalid', 'Yes'])
    def test_play_again_invalid_then_valid(self, mock_input):
        """Test invalid input followed by a valid 'yes'."""
        self.assertTrue(game.play_again())

    # -------------------------------
    # Game Flow & Hint Tests
    # -------------------------------
    @patch('random.randint', return_value=7)
    # Inputs: 1. Difficulty (1), 2. Winning Guess (7)
    @patch('builtins.input', side_effect=['1', '7']) 
    def test_guess_game_win_on_first_try(self, mock_input, mock_randint):
        """Test winning the game on the first try."""
        with patch('builtins.print') as mock_print:
            game.guess_game()
            mock_print.assert_any_call("\n🎉 CONGRATULATIONS! 🎉")

    @patch('random.randint', return_value=5)
    # Inputs: 1. Difficulty (1), 2. Too Low (3), 3. Too High (8), 4. Win (5)
    @patch('builtins.input', side_effect=['1', '3', '8', '5']) 
    def test_guess_game_multi_turn_hints(self, mock_input, mock_randint):
        """Test game flow, ensuring correct 'Too High' and 'Too Low' hints are given."""
        with patch('builtins.print') as mock_print:
            game.guess_game()
            
            # Assert that the correct hint messages were called during the game
            mock_print.assert_any_call("Too low! Try a higher number.")
            mock_print.assert_any_call("Too high! Try a lower number.")
            
            # The game should end with the win message
            mock_print.assert_any_call("You guessed the number 5 in 3 attempts!")

    @patch('random.randint', return_value=50)
    # Inputs: 1. Difficulty (2), 2. The exit command (exit)
    @patch('builtins.input', side_effect=['2', 'exit']) 
    def test_guess_game_exit(self, mock_input, mock_randint):
        """Test exiting the game reveals the secret number."""
        with patch('builtins.print') as mock_print:
            game.guess_game()
            mock_print.assert_any_call("\nThanks for playing! The secret number was 50.")
            
if __name__ == '__main__':
    unittest.main()
