import pyupbit

access = "4uxQVlPy2vfJmJUC8hxhxxm47XqXISA1XNv2qclU"          # 본인 값으로 변경
secret = "7HOh3lqS751dwrHOQoVjaBQR3z9ixQqBQUz8ZWjq"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-BTC"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회