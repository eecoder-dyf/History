@echo off
echo �رշ���
net stop "NvContainerLocalSystem"
timeout 2
echo ��������
net start "NvContainerLocalSystem"