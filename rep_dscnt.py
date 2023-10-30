import mysql.connector
import csv
import os

# データベース接続情報
DB_CONFIG = {
    'host': '--DBホスト',  # DBホスト
    'port': 000,  # 接続ポート
    'user': '--user',  # ユーザーID
    'password': '--pass',  # パスワード
    'database': '-db'  # DB名
}

target_path = "C:/Users/USERNAME/Documents/"  # 指定ディレクトリのpath

# CSVにエクスポートする関数


def export_to_csv(data, headers, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(data)


def main():
    # MySQLサーバーへの接続
    connection = mysql.connector.connect(**DB_CONFIG)
    cursor = connection.cursor()

    # テーブルからのデータの取得
    cursor.execute("SELECT * FROM m_dscnt")
    data = cursor.fetchall()
    headers = [i[0] for i in cursor.description]

    # /outputフォルダが存在しない場合、作成
    if not os.path.exists(target_path + "rep_dscnt/output"):
        os.makedirs(target_path + "rep_dscnt/output")

    # CSVファイルとして保存
    export_to_csv(
        data, headers, target_path + "rep_dscnt/output/m_dscnt_data.csv")

    cursor.close()
    connection.close()


if __name__ == "__main__":
    main()
