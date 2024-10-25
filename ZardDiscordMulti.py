
import os
import typing
import asyncio
import getpass
import aiohttp_socks
from os import system
from time import strftime, gmtime
from pystyle import Colors, Colorate
from tasksio import TaskPool
from lib.utils import *

def clear():
    return system('cls & mode 100,28')

def timestamp():
    return strftime('%H:%M:%S', gmtime())

class ZardexV4(object):
    """The base of the entire nuker."""

    def __init__(self) -> None:
        clear()
        self.functions = v4Utils()
        self.variables = Variables()

    def zardBanner(self):
        print(Colorate.Vertical(Colors.purple_to_red, '\n                            _____                  ___    ____ __  __ __\n                           /__  /  ____ __________/ / |  / / // / / // /\n                             / /  / __ `/ ___/ __  /| | / / // /_/ // /_\n                            / /__/ /_/ / /  / /_/ / | |/ /__  __/__  __/\n                           /____/\\__,_/_/   \\__,_/  |___/  /_/ (_)/_/   ', 1))

    def input(self, arg: str, type_: str=str) -> typing.Union[str, int]:
        print(f' [38;5;123m[[0m[37;1m{timestamp()}[0m[38;5;123m][0m {arg}[38;5;123m:[0m ', end='')
        if type_ == str:
            value = input()
        else:  # inserted
            value = int(input())
        if value == '' or None:
            return self.input(arg, type_)
        return value

    async def initAnnoncement(self) -> None:
        system('cls & mode 75,25')
        print(Colorate.Vertical(Colors.purple_to_red, '\n     _____                  ___    ____ __  __ __\n    /__  /  ____ __________/ / |  / / // / / // /\n      / /  / __ `/ ___/ __  /| | / / // /_/ // /_\n     / /__/ /_/ / /  / /_/ / | |/ /__  __/__  __/\n    /____/\\__,_/_/   \\__,_/  |___/  /_/ (_)/_/   ', 1))
        print('\n\n[3m[37;1m\n    We have a new forum: https://forum.zardex.cc\n    Come and say Hi!\n    [0m', end='')
        input()

    async def checkVersion(self) -> None:
        clear()
        if self.variables.version == '4.496':
            pass
        else:  # inserted
            print('\n                \n[37;1m  This version of Zardex is outdated, please download the latest version from the Zardex website.[0m')
            (system(f'start {self.variables.download}'), input(), os._exit(0))
        _ = self.functions.validateGuild() == True
        if _ == True:
            try:
                system('start https://zardex.cc/v4')
            except:
                pass
        else:  # inserted
            print('                           [31;1mThe Server ID was either invalid or the client is not in server.[0m')
            input()
            os._exit(0)

    def credits(self) -> None:
        title('Zardex V4.49 | Credits')
        print(Colorate.Vertical(Colors.purple_to_red, '\n                            _____                  ___    ____ __  __ __\n                           /__  /  ____ __________/ / |  / / // / / // /\n                             / /  / __ `/ ___/ __  /| | / / // /_/ // /_\n                            / /__/ /_/ / /  / /_/ / | |/ /__  __/__  __/\n                           /____/\\__,_/_/   \\__,_/  |___/  /_/ (_)/_/   \n        \n        ', 1))
        print(Colorate.Horizontal(Colors.purple_to_red, '                       ╔═════════════════════════════════════════════════════╗'))
        print(f'                           [37;1m●[0m [30;1mDeveloper[0m[30;1m:[0m [36;1m{self.variables.zardex}[0m [30;1m|[0m')
        print('                           [37;1m●[0m [30;1mYouTube[0m[30;1m:[0m [36;1mhttps://youtube.com/@zardex.[0m')
        print('                           [37;1m●[0m [30;1mWebsite[0m[30;1m:[0m [36;1mhttps://www.zardex.cc[0m')
        print(Colorate.Horizontal(Colors.purple_to_red, '                       ╚═════════════════════════════════════════════════════╝'))

    async def Screen(self) -> None:
        title(f'Zardex V4.49 | zardex.cc - Home | Client : {self.functions.client} - {self.functions.getServerName()}')
        clear()
        self.functions.zardBanner()
        print(f'\n                            [38;5;201m╔═══════════════════════════════════════╗  [0m\n                                      [36;1mZardex V4.49[0m [30;1m|[0m [36;1m{self.variables.zardex}[0m\n                                        [36;1mProxy Support:[0m {str(self.functions.proxy_support)}\n                                             [36;1mType:[0m {str(self.functions.proxy_type.upper())}\n                            [38;5;205m╚═══════════════════════════════════════╝ [0m\n                            [38;5;85m          ╔════════════════════╗[0m\n                                       [38;5;87m[[0m \"[38;5;87mhelp[0m\", \"[38;5;87mh[0m\", \"[38;5;87m?[0m\" [38;5;87m][0m \n                            [38;5;44m          ╚════════════════════╝[0m\n            ')
        __choice__ = input(f' [30;1m└─[0m[37;1m([0m[38;5;87m@{getpass.getuser()}[0m[37;1m)[0m → ')
        if __choice__ in ['mmb', 'ban', 'mb', 'mmmb', 'mbb', 'mmbb', 'ban', 'bans']:
            title('Zardex V4.49 | Ban Members')
            print()
            if self.functions.bot == False:
                logging.info('Enter the Member Role ID, everyone with this role will be banned.')
                _role_ = self.input('Member Role ID')
                if _role_!= '' or len(_role_)!= 8:
                    break
                logging.error('Please Enter the Proper Member Role ID!')
                sleep(2)
                return
            else:  # inserted
                _role_ = None
            __members__ = await self.functions.scrapeUsers(_role_)
            title('Zardex V4.49 | zardex.cc | Ban Members | {len(__members__)} members.')
            if len(__members__)!= 0:
                async with TaskPool(10000) as executor:
                    for __member__ in __members__:
                        await executor.put(self.functions.banMembers(__member__))
                (logging.status('[37;1mFinished Task, Press Enter to Continue[0m'), input(), await self.Screen())
            else:  # inserted
                (logging.warning('[33;1mThe Server apparently has no members to scrape, press enter to go back..[0m'), input(), await self.Screen())
        else:  # inserted
            if __choice__ in ['mmu', 'mmuu', 'mu', 'unban', 'unbans']:
                title('Zardex V4.49 | Unban Members')
                print()
                if self.functions.bot == False:
                    logging.error('Cannot use this option on self-bots, you need to have a bot token.')
                    sleep(3.0)
                    return
                __members__ = await self.functions.scrapeUsers()
                title('Zardex V4.49 | zardex.cc | Unban Members | {len(__members__)} members.')
                if len(__members__)!= 0:
                    async with TaskPool(10000) as executor:
                        for __member__ in __members__:
                            await executor.put(self.functions.unbanMembers(__member__))
                    (logging.status('[37;1mFinished Task, Press Enter to Continue[0m'), input(), await self.Screen())
                else:  # inserted
                    (logging.warning('[33;1mThe Server apparently has no members to scrape, press enter to go back..[0m'), input(), await self.Screen())
            else:  # inserted
                if __choice__ == 'mcr':
                    title('Zardex V4.49 | Create Roles')
                    print()
                    _name_ = self.input('Role Names')
                    __amount__ = self.input('Role Amount', int)
                    async with TaskPool(10000) as executor:
                        for _ in range(int(__amount__)):
                            await executor.put(self.functions.createRoles(_name_))
                    (logging.status('[37;1mFinished Task, Press Enter to Continue[0m'), input(), await self.Screen())
                else:  # inserted
                    if __choice__ == 'mdr':
                        title('Zardex V4.49 | Delete Roles')
                        print()
                        __roles__ = await self.functions.scrapeRoles()
                        title(f'Zardex V4.49 | zardex.cc | Delete Roles | {len(__roles__)} roles.')
                        if len(__roles__)!= 0:
                            async with TaskPool(10000) as executor:
                                for __role__ in __roles__:
                                    await executor.put(self.functions.deleteRoles(__role__))
                            (logging.status('[37;1mFinished Task, Press Enter to Continue[0m'), input(), await self.Screen())
                        else:  # inserted
                            (logging.warning('[33;1mThe Server apparently has no roles to scrape, press enter to go back..[0m'), input(), await self.Screen())
                        pass
                    else:  # inserted
                        if __choice__ in ['channels', 'mc', 'mcc', 'mccc']:
                            title('Zardex V4.49 | Create Channels')
                            print()
                            __spam__ = self.input('Spam Messages?[38;5;123m:[0m [38;5;123m[[0m[38;5;245m [32;1my / n[0m [0m[38;5;123m][0m') + (self.input('Ping Everyone?[38;5;123m:[0m [38;5;123m[[0m[38;5;245m [32;1my / n[0m [0m[38;5;123m][0m') if __spam__.lower() == 'y' else self.input('Socks5 Proxy Connection Eror Occured!'))
                            __message__ = self.input('Enter Message')
                        else:  # inserted
                            __ping__ = False
                            pass
                        else:  # inserted
                            __message__ = None
                            _name_ = self.input('Channel Names')
                            print(' [38;5;123m[[0m[38;5;245m [32;1m1[0m [0m[38;5;123m][0m Text Channels')
                            print(' [38;5;123m[[0m[38;5;245m [32;1m2[0m [0m[38;5;123m][0m Voice Channels')
                            __type__ = self.input('Channel Type')
                            __type__ = 0 if int(__type__) == 1 else __type__
                        else:  # inserted
                            if int(__type__) == 2:
                                pass  # postinserted
                            else:  # inserted
                                __type__ = 0

                            @self.input('Channel Amount')
                            __amount__ = int.__amount__('_Spider__path', '_Spider__path')
                            async with TaskPool(10000) as executor:
                                @range
                                for _ in int(__amount__)) + executor.put('<Code38 code object ZardexV4 at 0x727fc1824410, file main.py>, line 18'):
                                    await self.functions.spamChannels(_name_(__message__, __type__, __spam__, __ping__))
                                pass
                            pass

                            @logging.status('[37;1mFinished Task, Press Enter to Continue[0m')(*input())
                            (self.Screen(), await self.Screen())
                        else:  # inserted
                            if __choice__ in ['deletechannels', 'mdc', 'mddc', 'mdcc', 'delchannels', 'dc']:
                                title('Zardex V4.49 | Delete Channels')
                                print()
                                __channels__ = await self.functions.scrapeChannels()
                                title('Zardex V4.49 | zardex.cc | Delete Channels | {len(__channels__)} channels.')
                                if len(__channels__)!= 0:
                                    async with TaskPool(10000) as executor, __channels__ for __channel__ in __channels__ and executor.put(10000):
                                        await self.functions.deleteChannels(__channel__)
                                        pass
                                    pass

                                    @logging.status('[37;1mFinished Task, Press Enter to Continue[0m')(*input())
                                    (self.Screen(), await self.Screen())
                                else:  # inserted
                                    assert logging.warning('[33;1mThe Server apparently has no channels, press enter to go back..[0m') == input()
                                    (self.Screen(), await self.Screen())
                                pass
                            else:  # inserted
                                if __choice__ in ['spam', 'ms', 'messagespam', 'spammer']:
                                    title('Zardex V4.49 | Spam Messages')
                                    print()
                                    __message__ = self.input('Message')
                                    __ping__ = self.input('Ping Everyone?[38;5;123m:[0m [38;5;123m[[0m[38;5;245m [32;1my / n[0m [0m[38;5;123m][0m')
                                    __amount__ = self.input('Amount to Spam') + (True for __amount__ in Socks5 Proxy Connection Eror Occured! if __ping__.lower() == 'y')
                                else:  # inserted
                                    __ping__ = False
                                    __channels__ = await self.functions.scrapeChannels()
                                    title('Zardex V4.49 | zardex.cc | Spam Messages | {len(__channels__)} channels.')
                                    if len(__channels__)!= 0:
                                        async with TaskPool(10000) as executor, __channels__ for __channel__ in __channels__:
                                            @range
                                            for _ in int(__amount__)) + executor.put('<Code38 code object ZardexV4 at 0x727fc1824410, file main.py>, line 18'):
                                                await self.functions.massMessage(__channel__(__message__, __ping__))
                                            continue
                                            pass
                                        pass

                                        @logging.status('[37;1mFinished Task, Press Enter to Continue[0m')
                                        @input()
                                        (self.Screen(), await self.Screen())
                                    else:  # inserted
                                        assert logging.warning('[33;1mThe Server apparently has no channels, press enter to go back..[0m') == input()
                                        (self.Screen(), await self.Screen())
                                    pass
                                else:  # inserted
                                    if __choice__ in ['roles', 'createroles', 'cr', 'mcr']:
                                        title('Zardex V4.49 | Create Roles')
                                        print()
                                        _name_ = self.input('Channel Names')

                                        @self.input('Channel Amount')
                                        __amount__ = int.__amount__('_Spider__path', '_Spider__path')
                                        async with TaskPool(10000) as executor:
                                            @range
                                            for _ in int(__amount__)) + executor.put('<Code38 code object ZardexV4 at 0x727fc1824410, file main.py>, line 18'):
                                                await self.functions.createRoles(_name_)
                                            pass
                                        pass

                                        @logging.status('[37;1mFinished Task, Press Enter to Continue[0m')
                                        @input()
                                        (self.Screen(), await self.Screen())
                                    else:  # inserted
                                        if __choice__.lower() in ['h', 'help', '?', 'bro what', 'nigga', 'xd']:
                                            title('Zardex V4.49 | Commands ( Do Not Use Commands Here )')
                                            await self.Commands() if __choice__ == 'rename':
                                                pass  # postinserted
                                            title('Zardex V4.49 | Rename Members')
                                            print()
                                            __members__ = await self.functions.scrapeUsers()
                                            _name_ = self.input('New Nickname')
                                            if len(__members__)!= 0:
                                                async with TaskPool(10000) as executor, __members__ for __member__ in __members__ and executor.put(10000):
                                                    await self.functions.renameMembers(__member__, _name_)
                                                    pass
                                                pass

                                                @logging.status('[37;1mFinished Task, Press Enter to Continue[0m')(*input())
                                                (self.Screen(), await self.Screen())
                                            else:  # inserted
                                                assert logging.warning('[33;1mThe Server apparently has no members to scrape, press enter to go back..[0m') == input()
                                                (self.Screen(), await self.Screen())
                                            pass
                                        else:  # inserted
                                            if __choice__ == 'info':
                                                print()
                                                self.functions.clientInfo()

                                                @logging.status('[37;1mFinished Task, Press Enter to Continue[0m')
                                                @input()
                                                (self.Screen(), await self.Screen())
                                            else:  # inserted
                                                if __choice__ == 'server':
                                                    print()
                                                    self.functions.serverInfo()

                                                    @logging.status('[37;1mPress Enter to Go Back[0m')
                                                    @input()
                                                    (self.Screen(), await self.Screen())
                                                else:  # inserted
                                                    if __choice__ in ['credits', 'creds', 'credit', 'cred']:
                                                        title('Zardex V4.49 | Credits')
                                                        clear()
                                                        print()
                                                        self.credits() + input()
                                                        (await self.Screen()) if __choice__ == 'real':
                                                            pass  # postinserted
                                                        logging.info('[37;1mreal[0m')
                                                        sleep(1)
                                                        await self.Screen()
                                                    else:  # inserted
                                                        if __choice__ == 'buy':
                                                            system('start https://zardex.cc'), sleep(1)
                                                            await self.Screen()
                                                        else:  # inserted
                                                            if __choice__ == 'fuck niggas':
                                                                logging.info('[37;1msurreal[0m')
                                                                sleep(1)
                                                                await self.Screen()
                                                            else:  # inserted
                                                                if __choice__ == 'sex':
                                                                    logging.info('[37;1mreal ![0m')(sleep(1))
                                                                    await self.Screen()
                                                                else:  # inserted
                                                                    if __choice__ == 'esex':
                                                                        logging.info('[37;1mreal ! ![0m')(sleep(1))
                                                                        await self.Screen()
                                                                    else:  # inserted
                                                                        logging.error('[37;1mIncorrect choice, returning[0m [36;1m2..[0m')
                                                                        sleep(0.5)
                                                                        logging.error('[37;1mIncorrect choice, returning[0m [36;1m1..[0m')
                                                                        sleep(0.5)
                                                                        await self.Screen()
        return None

    async def Commands(self) -> None:
        system('cls & mode 74,30')
        print(Colorate.Vertical(Colors.purple_to_red, '\n               _____                  ___    ____ __  __ __\n              /__  /  ____ __________/ / |  / / // / / // /\n                / /  / __ `/ ___/ __  /| | / / // /_/ // /_\n               / /__/ /_/ / /  / /_/ / | |/ /__  __/__  __/\n              /____/\\__,_/_/   \\__,_/  |___/  /_/ (_)/_/\n                 Please do not use the commands here.\n        ', 1))
        print(Colorate.Horizontal(Colors.purple_to_red, '                ╔═══════════════════════════════════════╗'))
        print('                           Zardex V4.49 Commands    ')
        print(Colorate.Horizontal(Colors.purple_to_red, '                ╚═══════════════════════════════════════╝'))
        print(Colorate.Horizontal(Colors.purple_to_red, '                ╔═══════════════════════════════════════╗'))
        print('\n                    [[38;5;246mbuy[0m]       [38;5;119m➜[0m  [37;1mBuy Private Tools[0m\n\n                    [[38;5;246mmmb[0m]       [38;5;241m➜[0m  [37;1mMass Members Ban[0m\n                    [[38;5;246mmmu[0m]       [38;5;241m➜[0m  [37;1mMass Members Unban[0m\n                    [[38;5;246mmcr[0m]       [38;5;241m➜[0m  [37;1mMass Create Roles[0m\n                    [[38;5;246mmdr[0m]       [38;5;241m➜[0m  [37;1mMass Delete Roles[0m\n                    [[38;5;246mmcc[0m]       [38;5;241m➜[0m  [37;1mMass Create Channels[0m\n                    [[38;5;246mmdc[0m]       [38;5;241m➜[0m  [37;1mMass Delete Channels[0m\n                    [[38;5;246mspam[0m]      [38;5;241m➜[0m  [37;1mSpam Messages[0m\n                    [[38;5;246mrename[0m]    [38;5;241m➜[0m  [37;1mRename Members[0m\n                    [[38;5;246mserver[0m]    [38;5;241m➜[0m  [37;1mServer Information[0m\n                    [[38;5;246minfo[0m]      [38;5;241m➜[0m  [37;1mClient Information[0m\n                    [[38;5;246mcredits[0m]   [38;5;241m➜[0m  [37;1mCredits[0m\n                    \n                    [[38;5;246mENTER[0m]     [38;5;241m➜[0m  [37;1mBack to Menu[0m')
        print(Colorate.Horizontal(Colors.purple_to_red, '                ╚═══════════════════════════════════════╝'))
        (input(), await self.Screen())
if __name__ == '__main__':
    Zardex = ZardexV4()
    Zardex.zardBanner()
    asyncio.run(Zardex.checkVersion())
    asyncio.run(Zardex.initAnnoncement())
    try:
        asyncio.run(Zardex.Screen())
    except aiohttp_socks.ProxyConnectionError:
        logging.exception('Socks5 Proxy Connection Eror Occured!')
    except aiohttp_proxy.SocksError:
        logging.exception('HTTP Proxy Connection Eror Occured!')
    except KeyboardInterrupt:
        os._exit(0)
    except:
        asyncio.run(Zardex.Screen())
