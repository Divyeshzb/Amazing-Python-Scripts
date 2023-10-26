# Test generated by RoostGPT for test python-test-23 using AI Type Azure Open AI and AI Model roost-gpt4-32k

import unittest
from unittest.mock import patch
from TicTacToe import play_tic_tac_toe

class TestTicTacToe(unittest.TestCase):

    # Test that the Game is Initialized Properly
    @patch('TicTacToe.player_input', return_value=('X', 'O'))
    @patch('TicTacToe.choose_first', return_value='Player 1')
    @patch('TicTacToe.input', return_value='y')
    def test_GameInitialization(self, input_patch, choose_first_patch, player_input_patch):
        with patch('TicTacToe.print') as _:
            play_tic_tac_toe()
        choose_first_patch.assert_called_once()
        player_input_patch.assert_called_once()
        input_patch.assert_called_once_with('Are you ready to play? Enter y or n: ')

    # Test a Scenario Where Player Chooses Not to Play
    @patch('TicTacToe.player_input', return_value=('X', 'O'))
    @patch('TicTacToe.choose_first', return_value='Player 1')
    @patch('TicTacToe.input', return_value='n')
    def test_PlayerChooseNotToPlay(self, input_patch, choose_first_patch, player_input_patch):
        with patch('TicTacToe.print') as print_patch:
            play_tic_tac_toe()

        print_patch.assert_any_call("BYE! Have a good day.")

if __name__ == '__main__':
    unittest.main()