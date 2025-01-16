import flet as ft

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
