

# ----------------------------------------------------------------------------------------------------------------------#
"""     Script to ping and check whether any given IPs are active, also whether given set of
software are installed in the existing system ( like java, kubectl, aws etc)        """
# ----------------------------------------------------------------------------------------------------------------------#



#### took a reference from https://ashishpython.blogspot.com/2013/12/listing-all-installed-applications-on.html for how to get list of installed packages #############
# importing the module
from collections import namedtuple
from ctypes import byref, create_unicode_buffer, windll
from ctypes.wintypes import DWORD
from itertools import count
import os

# defined at http://msdn.microsoft.com/en-us/library/aa370101(v=VS.85).aspx
UID_BUFFER_SIZE = 39
PROPERTY_BUFFER_SIZE = 256
ERROR_MORE_DATA = 234
ERROR_INVALID_PARAMETER = 87
ERROR_SUCCESS = 0
ERROR_NO_MORE_ITEMS = 259
ERROR_UNKNOWN_PRODUCT = 1605

# diff propoerties of a product, not all products have all properties
PRODUCT_PROPERTIES = [
# u'ProductName',
                      # u'PackageCode',
                      # u'Transforms',
                      # u'AssignmentType',
                      # u'PackageName',
                      u'InstalledProductName',
                      # u'VersionString',
                      # u'RegCompany',
                      # u'RegOwner',
                      # u'ProductID',
                      # u'ProductIcon',
                      # u'InstallLocation',
                      # u'InstallSource',
                      # u'InstallDate',
                      # u'Publisher',
                      # u'LocalPackage',
                      # u'HelpLink',
                      # u'HelpTelephone',
                      # u'URLInfoAbout',
                      # u'URLUpdateInfo',
                      ]

# class to be used for python users :)
Product = namedtuple('Product', PRODUCT_PROPERTIES)


def get_property_for_product(product, property, buf_size=PROPERTY_BUFFER_SIZE):
    """Retruns the value of a fiven property from a product."""
    property_buffer = create_unicode_buffer(buf_size)
    size = DWORD(buf_size)
    result = windll.msi.MsiGetProductInfoW(product, property, property_buffer,
                                           byref(size))
    if result == ERROR_MORE_DATA:
        return get_property_for_product(product, property,
                                        2 * buf_size)
    elif result == ERROR_SUCCESS:
        return property_buffer.value
    else:
        return None


def populate_product(uid):
    """Return a Product with the different present data."""
    properties = []
    for property in PRODUCT_PROPERTIES:
        properties.append(get_property_for_product(uid, property))
    return Product(*properties)


def get_installed_products_uids():
    """Returns a list with all the different uid of the installed apps."""
    # enum will return an error code according to the result of the app
    products = []
    for i in count(0):
        uid_buffer = create_unicode_buffer(UID_BUFFER_SIZE)
        result = windll.msi.MsiEnumProductsW(i, uid_buffer)
        if result == ERROR_NO_MORE_ITEMS:
            # done interating over the collection
            break
        products.append(uid_buffer.value)
    return products


def get_installed_products():
    """Returns a collection of products that are installed in the system."""
    products = []
    for puid in get_installed_products_uids():
        products.append(populate_product(puid))
    return products

#################################################################################################################


def clear_screen():
    input('Press Enter->')
    os.system('cls')


if __name__ == '__main__':
    while True:
        print('\n\nEnter your choice-\n1.Ping IP Address \n2.Check package installed or not \n3.Exit')
        n=int(input())
        if n==1:
            # from pythonping import ping
            # ping('197.12.12.13', verbose=True)
            #

            ipaddr = input('Enter the IP address:(x.x.x.x)')
            stream = os.popen('ping -n 4 {}'.format(ipaddr))
            output = stream.read()
            # if '0 received' in output:
            #     # print('IP unreachable')
            # else:
            #     print('IP reachable')
            print(output)
            clear_screen()

        elif n==2:
            check_pkg=input('Enter package name.\n').lower()
            apps = get_installed_products()
            for app in apps:
                # print(app)
                package=str(app.InstalledProductName).lower()
                # print(package)
                if (package.find(check_pkg) == -1):
                    pass
                else:
                    print(f"{check_pkg} package is present.")
                    clear_screen()
                    break

            else:
                print('Package is not installed.')
                clear_screen()
        elif n==3:
            break
        else:
            print('Enter the corrent choice.')
            # clear_screen()


