import csv
import mysql.connector
import os

# CSVファイルのパス
CSV_PATH = "C:\\Users\\USERNAME\\Documents\\write_dscnt\\new_data\\m_dscnt_data.csv"  # 監視ターゲットファイルパス

# データベース接続情報
DB_CONFIG = {
    'host': '--DBホスト',  # DBホスト
    'port': 000,  # 接続ポート
    'user': '--user',  # ユーザーID
    'password': '--pass',  # パスワード
    'database': '-db'  # DB名
}


def main():
    # CSVファイルの存在確認
    if not os.path.exists(CSV_PATH):
        print("CSV file does not exist. Exiting.")
        return

    # CSVデータの読み込み
    with open(CSV_PATH, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        headers = next(reader)
        data = list(reader)

    # MySQLサーバーへの接続
    connection = mysql.connector.connect(**DB_CONFIG)
    cursor = connection.cursor()

    # 対象テーブルのレコードを全削除
    cursor.execute("DELETE FROM m_dscnt")

    # データの書き込み
    for row in data:
        cursor.execute(
            "INSERT INTO m_dscnt (DSC_ID, PRD_ID, DSC_AMT) VALUES (%s, %s, %s)", row)

    # トランザクションのコミット
    connection.commit()

    cursor.close()
    connection.close()

    # CSVファイルの削除
    os.remove(CSV_PATH)


if __name__ == "__main__":
    main()
