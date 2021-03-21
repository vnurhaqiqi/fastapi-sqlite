import bcrypt


def get_hashed_password(plain_text_password):
    return bcrypt.hashpw(plain_text_password, bcrypt.gensalt())


def verify_password(plain_text_password, hashed_password):
    return bcrypt.checkpw(plain_text_password, hashed_password)
