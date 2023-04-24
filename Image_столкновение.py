def hit_paddle(self, pos):
    paddle_pos = self.gamerootCanvas.bbox(self.paddle.id)
    if pos[1] >= paddle_pos[1] and pos[1] <= paddle_pos[3]:
        if pos[0] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            return True
    return False