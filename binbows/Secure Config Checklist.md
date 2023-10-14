# Secure Conifg (according to a linux person)

### 1. Check Users and their priveleges (refer to the machine's README for all the authorized users and permissions (use Get-LocalUser for all local users, for user permissions check AD Users and Computers)

`Get-LocalUser`

### 2. Check the Windows Firewall. Make sure it's enabled and blocks all ports that are not required for the services

### 3. Enforce Safe Passwords (refer to https://learn.microsoft.com/en-us/powershell/module/activedirectory/set-addefaultdomainpasswordpolicy?view=windowsserver2022-ps for more info on params)
`Set-ADDefaultDomainPasswordPolicy -Identity <domain> -LockoutDuration 00:10:00 -LockoutObservationWindow 00:10:00 -ComplexityEnabled $True -ReversibleEncryptionEnabled $False -MaxPasswordAge 90.00:00:00 -MinPasswordAge 05.00:00:00 -MinPasswordLength 12`

### 4. Change the user passwords (to change a specific user with a password being hidden, use the following command where USERNAME is the user's name)

`net user USERNAME *`

### Answer Key for the Mario machine that has some useful tips

https://drive.google.com/file/d/16Bggptd-y-WR8CFA2BhkGPrLSV0yzqaO/view
h e l p
