def fake_predict(user_age):
    if user_age > 10:
        prediction = "survive (over 10)"
    else:
        prediction = "Super Survive (under 10)"
    return prediction