def baho_aniqla(ball):
    if ball >= 90:
        return "A'lo"
    elif ball >= 70:
        return "Yaxshi"
    elif ball >= 50:
        return "Qoniqarli"
    else:
        return "Qoniqarsiz"


def ortacha_hisobla(balllar):
    return sum(balllar) / len(balllar)


def eng_yaxshi_ball(balllar):
    return max(balllar)