# Secure Conifg (according to a linux person)

### 1. Check Users and their priveleges (refer to the machine's README for all the authorized users and permissions (use Get-LocalUser for all local users, for user permissions check AD Users and Computers)

`Get-LocalUser`

### 2. Check the Windows Firewall. Make sure it's enabled and blocks all ports that are not required for the services

### 3. Enforce Safe Passwords (refer to https://learn.microsoft.com/en-us/powershell/module/activedirectory/set-addefaultdomainpasswordpolicy?view=windowsserver2022-ps for more info on params)
`Set-ADDefaultDomainPasswordPolicy -Identity <domain> -LockoutDuration 00:10:00 -LockoutObservationWindow 00:10:00 -ComplexityEnabled $True -ReversibleEncryptionEnabled $False -MaxPasswordAge 90.00:00:00 -MinPasswordAge 05.00:00:00 -MinPasswordLength 12`

### 4. Change the user passwords (to change a specific user with a password being hidden, use the following command where USERNAME is the user's name)

`net user USERNAME *`

### #5 Check group policies and make sure they're in accordance to the README

### #6 Remove SMBv1 ffs it's scary do you want to ger wannacry or something? 

Use this command to see if it's enabled

`Get-WindowsOptionalFeature -Online -FeatureName SMB1Protocol`

Use this to disable it

`Disable-WindowsOptionalFeature -Online -FeatureName SMB1Protocol`

### #7 Monitor Processes with the Process Explorer

### Answer Key for the Mario machine that has some useful tips

https://drive.google.com/file/d/16Bggptd-y-WR8CFA2BhkGPrLSV0yzqaO/view

### as well as this cool holy grail file https://downloads.cisecurity.org/#/ 

h e l p im just a little eepy linux guy tf is a gui
