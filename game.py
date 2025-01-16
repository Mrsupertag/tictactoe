import flet as ft
import math

def main(page: ft.Page):
    page.title = "Tic Tac Toe"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = ft.colors.BLACK

    def start_game(mode):
        if mode == "AI":
            ai_game(page)
        elif mode == "Two Player":
            two_player_game(page)

    def main_menu():
        page.controls.clear()
        heading = ft.Text(value="Tic Tac Toe", size=70, color=ft.colors.WHITE, weight=ft.FontWeight.BOLD)
        label = ft.Text(value="Select a mode", size=30, color=ft.colors.WHITE)

        ai_button = ft.Container(
            content=ft.Row([ft.Text("Play with AI", size=20, color=ft.colors.BLACK)], alignment=ft.MainAxisAlignment.CENTER),
            on_click=lambda e: start_game("AI"),
            width=200,
            height=200,
            bgcolor=ft.colors.GREY,
            border_radius=100,
            alignment=ft.alignment.center
        )

        two_player_button = ft.Container(
            content=ft.Row([ft.Text("Two Player", size=20, color=ft.colors.BLACK)], alignment=ft.MainAxisAlignment.CENTER),
            on_click=lambda e: start_game("Two Player"),
            width=200,
            height=200,
            bgcolor=ft.colors.GREY,
            border_radius=100,
            alignment=ft.alignment.center
        )

        menu = ft.Column(
            [ft.Container(content=heading, alignment=ft.alignment.center),
             ft.Container(content=label, alignment=ft.alignment.center),
             ft.Row([ai_button, two_player_button], alignment=ft.MainAxisAlignment.CENTER, spacing=50)],
            alignment=ft.MainAxisAlignment.CENTER
        )

        page.add(menu)
        page.update()

    def ai_game(page):
        board = [""] * 9
        current_player = "X"
        game_over = False

        heading = ft.Text(value="Tic Tac Toe", size=70, color=ft.colors.WHITE, weight=ft.FontWeight.BOLD)

        def check_winner(board):
            for combo in [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]:
                if board[combo[0]] == board[combo[1]] == board[combo[2]] != "":
                    return board[combo[0]]
            if "" not in board:
                return "Draw"
            return None

        def check_draw(board):
            return "" not in board

        def minimax(board, depth, is_maximizing):
            winner = check_winner(board)
            if winner == "O":
                return 1
            elif winner == "X":
                return -1
            elif check_draw(board):
                return 0

            if is_maximizing:
                best_score = -math.inf
                for i in range(9):
                    if board[i] == "":
                        board[i] = "O"
                        score = minimax(board, depth + 1, False)
                        board[i] = ""
                        best_score = max(score, best_score)
                return best_score
            else:
                best_score = math.inf
                for i in range(9):
                    if board[i] == "":
                        board[i] = "X"
                        score = minimax(board, depth + 1, True)
                        board[i] = ""
                        best_score = min(score, best_score)
                return best_score

        def ai_move(board):
            best_score = -math.inf
            move = None
            for i in range(9):
                if board[i] == "":
                    board[i] = "O"
                    score = minimax(board, 0, False)
                    board[i] = ""
                    if score > best_score:
                        best_score = score
                        move = i
            if move is not None:
                board[move] = "O"

        def update_ui():
            for btn in buttons:
                btn.content.controls[0].value = board[btn.data]
                btn.update()

        def handle_click(e):
            nonlocal current_player, game_over
            if not game_over and board[e.control.data] == "":
                board[e.control.data] = current_player
                update_ui()
                winner = check_winner(board)
                if winner:
                    if winner == "Draw":
                        heading.value = "It's a draw!"
                        page.title = "It's a draw!"
                    else:
                        heading.value = f"{winner} Won!"
                        page.title = f"{winner} Won!"
                    page.snack_bar = ft.SnackBar(ft.Text(heading.value))
                    page.snack_bar.open = True
                    game_over = True
                    page.update()
                    return

                if not game_over:
                    current_player = "O"
                    ai_move(board)
                    update_ui()
                    winner = check_winner(board)
                    if winner:
                        if winner == "Draw":
                            heading.value = "It's a draw!"
                            page.title = "It's a draw!"
                        else:
                            heading.value = f"{winner} Won!"
                            page.title = f"{winner} Won!"
                        page.snack_bar = ft.SnackBar(ft.Text(heading.value))
                        page.snack_bar.open = True
                        game_over = True
                        page.update()
                        return

                    current_player = "X"

        buttons = []

        grid = ft.Column(alignment=ft.MainAxisAlignment.CENTER)

        for row in range(3):
            row_controls = []
            for col in range(3):
                index = row * 3 + col
                btn = ft.Container(
                    content=ft.Row([ft.Text(board[index], size=50)], alignment=ft.MainAxisAlignment.CENTER),
                    on_click=handle_click,
                    data=index,
                    width=120,
                    height=120,
                    bgcolor=ft.colors.GREY,
                    border_radius=60,
                    alignment=ft.alignment.center
                )
                buttons.append(btn)
                row_controls.append(btn)
            grid.controls.append(ft.Row(row_controls, spacing=10, alignment=ft.MainAxisAlignment.CENTER))

        page.controls.clear()
        page.add(ft.Column([ft.Container(content=heading, alignment=ft.alignment.center), ft.Container(content=grid, alignment=ft.alignment.center, padding=20)], alignment=ft.MainAxisAlignment.CENTER))
        page.update()

    def two_player_game(page):
        board = [""] * 9
        current_player = "X"
        game_over = False

        heading = ft.Text(value="Tic Tac Toe", size=70, color=ft.colors.WHITE, weight=ft.FontWeight.BOLD)

        def check_winner(board):
            for combo in [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]:
                if board[combo[0]] == board[combo[1]] == board[combo[2]] != "":
                    return board[combo[0]]
            if "" not in board:
                return "Draw"
            return None

        def check_draw(board):
            return "" not in board

        def update_ui():
            for btn in buttons:
                btn.content.controls[0].value = board[btn.data]
                btn.update()

        def handle_click(e):
            nonlocal current_player, game_over
            if not game_over and board[e.control.data] == "":
                board[e.control.data] = current_player
                update_ui()
                winner = check_winner(board)
                if winner:
                    if winner == "Draw":
                        heading.value = "It's a draw!"
                        page.title = "It's a draw!"
                    else:
                        heading.value = f"{winner} Won!"
                        page.title = f"{winner} Won!"
                    page.snack_bar = ft.SnackBar(ft.Text(heading.value))
                    page.snack_bar.open = True
                    game_over = True
                    page.update()
                    return

                current_player = "O" if current_player == "X" else "X"

        buttons = []

        grid = ft.Column(alignment=ft.MainAxisAlignment.CENTER)

        for row in range(3):
            row_controls = []
            for col in range(3):
                index = row * 3 + col
                btn = ft.Container(
                    content=ft.Row([ft.Text(board[index], size=50)], alignment=ft.MainAxisAlignment.CENTER),
                    on_click=handle_click,
                    data=index,
                    width=120,
                    height=120,
                    bgcolor=ft.colors.GREY,
                    border_radius=60,
                    alignment=ft.alignment.center
                )
                buttons.append(btn)
                row_controls.append(btn)
            grid.controls.append(ft.Row(row_controls, spacing=10, alignment=ft.MainAxisAlignment.CENTER))

        page.controls.clear()
        page.add(ft.Column([ft.Container(content=heading, alignment=ft.alignment.center), ft.Container(content=grid, alignment=ft.alignment.center, padding=20)], alignment=ft.MainAxisAlignment.CENTER))
        page.update()

    main_menu()

if __name__ == "__main__":
    ft.app(target=main)
