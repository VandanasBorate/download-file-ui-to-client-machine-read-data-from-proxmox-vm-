# import os
# import paramiko
# from flask import Flask, send_file, jsonify, render_template


#  # SSH connection details 
# hostname = '192.168.1.150'  # Proxmox host IP address
# port = 22  # SSH port
# username = 'linux'  # SSH username
# password = '1234'  # SSH password


# # Flask App Setup
# app = Flask(__name__)

# # SSH Client Connection
# def create_ssh_client(hostname, port, username, password):
#     try:
#         ssh_client = paramiko.SSHClient()
#         ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#         ssh_client.connect(hostname, port=port, username=username, password=password)
#         return ssh_client
#     except Exception as e:
#         print(f"Error creating SSH connection: {str(e)}")
#         return None

# # Function to download a file from Proxmox
# def download_file(ssh_client, file_path, local_path):
#     try:
#         sftp_client = ssh_client.open_sftp()
#         sftp_client.get(file_path, local_path)  # Download file to local path
#         sftp_client.close()
#         return local_path
#     except Exception as e:
#         print(f"Error downloading file {file_path}: {str(e)}")
#         return None

# # Route to check if file exists in Proxmox
# @app.route('/check_file/<filename>', methods=['GET'])
# def check_file(filename):
#     # Define VM download directory and SSH connection details
#     vm_download_dir = "/home/linux/Downloads"  # Proxmox VM directory containing ISO files
#     remote_file_path = os.path.join(vm_download_dir, filename)
#     # Create SSH client
#     ssh_client = create_ssh_client(hostname, port, username, password)
    
#     if ssh_client:
#         # Check if the file exists in Proxmox VM
#         sftp_client = ssh_client.open_sftp()
#         file_exists = False
#         try:
#             sftp_client.stat(remote_file_path)  # Check if file exists on VM
#             file_exists = True
#         except FileNotFoundError:
#             file_exists = False
#         sftp_client.close()

#         ssh_client.close()

#         return jsonify({'exists': file_exists})
#     else:
#         return jsonify({'exists': False})

# # Route to serve the UI (index.html)
# @app.route('/')
# def index():
#     return render_template('webserver.html')  # Serve the HTML UI

# # Route to download the file from Proxmox
# @app.route('/download/<filename>', methods=['GET'])
# def download(filename):
#     # Define VM download directory and SSH connection details
#     vm_download_dir = "/home/linux/Downloads"
#     local_file_path = f"/home/innuser002/flask_app_vm/backup/{filename}"  # Store downloaded file locally
#     # Create SSH client
#     ssh_client = create_ssh_client(hostname, port, username, password) 
#     if ssh_client:
#         # Path to the file in VM's download directory
#         remote_file_path = os.path.join(vm_download_dir, filename)
        
#         # Download the file from Proxmox VM to local machine
#         downloaded_file = download_file(ssh_client, remote_file_path, local_file_path)
        
#         # Close SSH connection after use
#         ssh_client.close()

#         if downloaded_file:
#             # Send the downloaded file to the client
#             return send_file(downloaded_file, as_attachment=True)
#         else:
#             return jsonify(error=f"Error downloading the file: {filename}"), 500
#     else:
#         return jsonify(error="SSH connection failed."), 500

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000, debug=True)







# import os
# import paramiko
# from flask import Flask, jsonify, render_template, Response
# from io import BytesIO

# # Flask App Setup
# app = Flask(__name__)

# # SSH Client Connection
# def create_ssh_client(hostname, port, username, password):
#     try:
#         ssh_client = paramiko.SSHClient()
#         ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#         ssh_client.connect(hostname, port=port, username=username, password=password)
#         return ssh_client
#     except Exception as e:
#         print(f"Error creating SSH connection: {str(e)}")
#         return None

# # Function to stream the file from Proxmox VM
# def stream_file_from_proxmox(ssh_client, file_path):
#     try:
#         sftp_client = ssh_client.open_sftp()
#         file = sftp_client.open(file_path, 'rb')  # Open the file in binary read mode
#         file_data = file.read()  # Read the file data into memory
#         file.close()
#         sftp_client.close()

#         # Return a BytesIO buffer containing the file content
#         return BytesIO(file_data)
#     except Exception as e:
#         print(f"Error downloading file {file_path}: {str(e)}")
#         return None

# # Route to check if the file exists in Proxmox
# @app.route('/check_file/<filename>', methods=['GET'])
# def check_file(filename):
#     # Define VM download directory and SSH connection details
#     vm_download_dir = "/home/linux/Downloads"  # Proxmox VM directory containing ISO files
#     remote_file_path = os.path.join(vm_download_dir, filename)

#     # SSH connection details (replace with your Proxmox host's credentials)
#     hostname = '192.168.1.150'  # Proxmox host IP address
#     port = 22  # SSH port
#     username = 'linux'  # SSH username
#     password = '1234'  # SSH password

#     # Create SSH client
#     ssh_client = create_ssh_client(hostname, port, username, password)

#     if ssh_client:
#         # Check if the file exists in Proxmox VM
#         sftp_client = ssh_client.open_sftp()
#         file_exists = False
#         try:
#             sftp_client.stat(remote_file_path)  # Check if file exists on VM
#             file_exists = True
#         except FileNotFoundError:
#             file_exists = False
#         sftp_client.close()

#         ssh_client.close()

#         return jsonify({'exists': file_exists})
#     else:
#         return jsonify({'exists': False})

# # Route to serve the UI (index.html)
# @app.route('/')
# def index():
#     return render_template('webserver.html')  # Serve the HTML UI

# # Route to download the file from Proxmox and stream it directly to the client
# @app.route('/download/<filename>', methods=['GET'])\
# def download(filename):
#     # Define VM download directory and SSH connection details
#     vm_download_dir = "/home/linux/Downloads"

#     # SSH connection details (replace with your Proxmox host's credentials)
#     hostname = '192.168.1.150'  # Proxmox host IP address
#     port = 22  # SSH port
#     username = 'linux'  # SSH username
#     password = '1234'  # SSH password

#     # Create SSH client
#     ssh_client = create_ssh_client(hostname, port, username, password)

#     if ssh_client:
#         # Path to the file in VM's download directory
#         remote_file_path = os.path.join(vm_download_dir, filename)

#         # Stream the file from Proxmox VM to the client directly
#         file_data = stream_file_from_proxmox(ssh_client, remote_file_path)

#         # Close SSH connection after use
#         ssh_client.close()

#         if file_data:
#             # Send the file as a response to the client (browser will handle the download)
#             return Response(file_data,
#                             mimetype='application/octet-stream',
#                             headers={'Content-Disposition': f'attachment; filename={filename}'})
#         else:
#             return jsonify(error=f"Error streaming the file: {filename}"), 500
#     else:
#         return jsonify(error="SSH connection failed."), 500

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000, debug=True)




import os
from flask import Flask, jsonify, render_template, Response, send_from_directory

# Flask App Setup
app = Flask(__name__)

# Function to check if the file exists on the NFS mount
def check_file_exists(file_path):
    return os.path.isfile(file_path)

# Route to check if the file exists in the NFS share
@app.route('/check_file/<filename>', methods=['GET'])
def check_file(filename):
    # Define NFS mount directory (client machine's mounted NFS share path)
    nfs_mount_dir = "/mnt/nfs_client"  # The mounted NFS share path on the client machine
    remote_file_path = os.path.join(nfs_mount_dir, filename)

    # Check if the file exists in the NFS mount directory
    file_exists = check_file_exists(remote_file_path)

    return jsonify({'exists': file_exists})

# Route to serve the UI (index.html)
@app.route('/')
def index():
    return render_template('webserver.html')  # Serve the HTML UI

# Route to download the file from the NFS share and stream it directly to the client
@app.route('/download/<filename>', methods=['GET'])
def download(filename):
    # Define NFS mount directory (client machine's mounted NFS share path)
    nfs_mount_dir = "/mnt/nfs_client"  # The mounted NFS share path on the client machine
    remote_file_path = os.path.join(nfs_mount_dir, filename)

    # Check if the file exists on the NFS mount
    if check_file_exists(remote_file_path):
        # Use Flask's send_from_directory to serve the file
        return send_from_directory(nfs_mount_dir, filename, as_attachment=True)
    else:
        return jsonify(error="File not found."), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
