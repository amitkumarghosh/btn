from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import sqlite3

import pandas as pd


import streamlit as st

# database_path = 'apps_dbase/Zero_Hrs_Data.sqlite'
# conn = sqlite3.connect(database_path)

# cursor = conn.cursor()

# cursor.execute('SELECT * FROM Moodle_Data WHERE Attendance_Status IS NOT NULL')

# # Fetch the results
# results = cursor.fetchall()

# # ae.show_send_email()


    
def main():
    st.title("Send email Page")
    if st.button("Send Validation Data Now"):
        
        sender_email = 'student.attendance@anudip.org'
        receiver_emails = ['student.attendance@anudip.org']
        subject = 'Academic Excellence - Validation Data - Manual Shared'
        body = 'Hi,This email contains all the validated student data \n~ Amit Kumar Ghosh'
        csv_content = generate_moodle_data_csv()
        send_email(sender_email, receiver_emails, subject, body, csv_content)

    #     sender_email2 = 'student.attendance@anudip.org'
    #     receiver_emails2 = ['amit.ghosh@anudip.org']
    #     subject2 = 'Academic Excellence - Validation Data and Updated Credentials - Manual Shared'
    #     body2 = 'Hi,This email contains all the upd cred data \n~ Amit Kumar Ghosh'
    #     csv_content = generate_moodle_data_csv()
    #     csv_content2 = generate_user_credential_csv()

    # send_email2(sender_email2, receiver_emails2, subject2, body2, csv_content,csv_content2)
    # st.success('Email sent successfully!')

def send_email(sender_email, receiver_emails, subject, body, csv_content):
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = ', '.join(receiver_emails)  # Join multiple recipients with comma
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    part = MIMEBase('application', 'octet-stream')
    part.set_payload(csv_content.encode('utf-8'))
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename=AE_Validated_Students_Data.csv')
    message.attach(part)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:  # Use port 465 for SSL
        server.login(sender_email, 'zdmq fmfu hgfe xblt')  # Replace with your email password
        server.sendmail(sender_email, receiver_emails, message.as_string())

# def send_email2(sender_email2, receiver_emails2, subject2, body2, csv_attachment, csv_attachment2):
#     message = MIMEMultipart()
#     message['From'] = sender_email2
#     message['To'] = ', '.join(receiver_emails2)  # Join multiple recipients with comma
#     message['Subject'] = subject2
#     message.attach(MIMEText(body2, 'plain'))

#     part = MIMEBase('application', 'octet-stream')
#     part.set_payload(csv_attachment.encode('utf-8'))
#     encoders.encode_base64(part)
#     part.add_header('Content-Disposition', 'attachment; filename=AE_Validated_Students_Data.csv')
#     message.attach(part)

#     part2 = MIMEBase('application', 'octet-stream')
#     part2.set_payload(csv_attachment2.encode('utf-8'))
#     encoders.encode_base64(part2)
#     part2.add_header('Content-Disposition', 'attachment; filename=AE_Updated_cread_Data.csv')
#     message.attach(part2)

#     with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:  # Use port 465 for SSL
#         server.login(sender_email2, 'zdmq fmfu hgfe xblt')  # Replace with your email password
#         server.sendmail(sender_email2, receiver_emails2, message.as_string())



def generate_moodle_data_csv():
    moodle_data = get_moodle_data()
    csv_content = moodle_data.to_csv(index=False)
    return csv_content

# def generate_user_credential_csv():
#     user_data = get_user_data()
#     csv_content2 = user_data.to_csv(index=False)
#     return csv_content2



# database_path = 'apps_dbase/Zero_Hrs_Data.sqlite'
# conn = sqlite3.connect(database_path)

# cursor = conn.cursor()

# cursor.execute('SELECT * FROM Moodle_Data WHERE Attendance_Status IS NOT NULL')

# # Fetch the results
# results = cursor.fetchall()

# Function to get attendee data from SQLite database
def get_moodle_data():
    database_path = 'apps_dbase/Zero_Hrs_Data.sqlite'
    conn = sqlite3.connect(database_path)
    
    df = pd.read_sql_query("select * from Moodle_Data where Attendance_Status IS NOT NULL", conn)
    st.write(df)
    conn.close()
    return df

# def get_user_data():
#     conn = sqlite3.connect('Zero_Hrs_Data.sqlite')
#     df2 = pd.read_sql_query("select * from User_Credentials", conn)
#     conn.close()
#     return df2

if __name__ == "__main__":
    main()
