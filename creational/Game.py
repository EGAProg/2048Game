from tkinter import messagebox

class Game:
    def __init__(self, board):
        self.board = board
        self.end = False
        self.won = False

    def start(self):
        self.board.random_cell()
        self.board.random_cell()
        self.board.paintGrid()
        self.board.window.bind('<Key>', self.link_keys)
        self.board.window.mainloop()
    
    def link_keys(self, event):
        if self.end or self.won:
            return

        self.board.compress = False
        self.board.merge = False
        self.board.moved = False

        presed_key=event.keysym

        if presed_key == 'Up':
            self.board.transpose()
            self.board.compressGrid()
            self.board.mergeGrid()
            self.board.moved = self.board.compress or self.board.merge
            self.board.compressGrid()
            self.board.transpose()

        elif presed_key == 'Down':
            self.board.transpose()
            self.board.reverse()
            self.board.compressGrid()
            self.board.mergeGrid()
            self.board.moved = self.board.compress or self.board.merge
            self.board.compressGrid()
            self.board.reverse()
            self.board.transpose()

        elif presed_key == 'Left':
            self.board.compressGrid()
            self.board.mergeGrid()
            self.board.moved = self.board.compress or self.board.merge
            self.board.compressGrid()

        elif presed_key == 'Right':
            self.board.reverse()
            self.board.compressGrid()
            self.board.mergeGrid()
            self.board.moved = self.board.compress or self.board.merge
            self.board.compressGrid()
            self.board.reverse()
        else:
            pass

        self.board.paintGrid()

        flag = 0
        for i in range(4):
            for j in range(4):
                if(self.board.gridCell[i][j] == 2048):
                    flag=1
                    break

        if(flag == 1): #found 2048
            self.won=True
            messagebox.showinfo('2048', message='You Won!')
            
            return

        for i in range(4):
            for j in range(4):
                if self.board.gridCell[i][j] == 0:
                    flag = 1
                    break

        if not (flag or self.board.can_merge()):
            self.end = True
            messagebox.showinfo('2048','Game Over!')
            

        if self.board.moved:
            self.board.random_cell()
        
        self.board.paintGrid()
    