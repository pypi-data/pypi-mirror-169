# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['chancery']

package_data = \
{'': ['*']}

install_requires = \
['needly>=2.5.61,<3.0.0']

entry_points = \
{'console_scripts': ['chancery = chancery.chancery:main']}

setup_kwargs = {
    'name': 'chancery',
    'version': '0.9.6',
    'description': 'Chancery is a simple text editor with predefined openQA snippets.',
    'long_description': "Chancery\n########\n\n**Chancery** is a very simple text editor for `openQA <https://open.qa>`_, i.e. allows to type text, save and open files. However, its main purpose is to speed up the development of openQA test scripts so it does not specialize in text typing in the first place. Its main strength is that it comes with a library of openQA command snippets that you can quickly insert using the *menu items* or *keyboard shortcuts*.   \n\nThe current version (0.9) offers almost all snippets that are most frequently used in Fedora openQA scripts. The future versions will provide more and more snippets until the whole openQA `TestApi <http://open.qa/api/testapi/>`_ is covered. If you are new to openQA scripting, you might want to read the `openQA TestApi <http://open.qa/api/testapi/>`_ to understand, how specific methods (snippets) work and what you can expect from them. \n\nHow to use the application\n==========================\n\n* Type in the text area.\n* Insert snippets at a cursor position using **Quick actions**, **Menu**, or **Keyboard shortcuts**.\n\nHow to start with openQA scripting\n==================================\n\n1. Each script needs to be enclosed in the `sub {}` structure, or it will not work in the openQA engine. The **Create file layout** button in the **Quick actions** will insert the snippet for you.\n\n2. Each script needs to have a subroutine called `test_flags` to set test flags for the script. The **Set test flags** button in the **Quick actions** will insert the snippet for you with all the test flags switched off. To switch on the flag, change its value to `1`. Note, that some of the test flags contradict each other, such as `no_rollback` or `always_rollback` so pay attention to the settings. You can also delete the unused flags for better readability.\n\nHow to work with snippets\n=========================\n\nObligatory arguments\n--------------------\nUsually, the methods use **obligatory arguments**, further called *arguments*. These are presented as **perl variables**, such as `$needlematch` or `$text`. \nYou can either define these variables previously, or replace the references with expected values.\n\nNon-obligatory arguments\n------------------------\n\nThe testAPI methods use various configuration options. When these are left out, the method then works with the default settings, which is mostly fine.\nThe snippets, however, provide all such configuration variables using the default values so they can be modified to suit the users' needs without having to consult the documentation all the time. If you *do not need to alter an option* you can leave it as is, or delete it from the snippet for better readability. \n\nExamples\n========\n\nCreate a skeleton file\n----------------------\n\n1. Click **Create file layout** on the **Quick actions** menu.\n2. Navigate to the end of the file.\n3. Click **Set test flags** on the **Quick actions** menu.\n4. Change the values to **1** for flags you want to set.\n\nUsing the skeleton file to create a perl module\n-----------------------------------------------\n\n1. Create a skeleton file (see above).\n2. Add an event or command using the prebuilt snippets.\n3. Edit command snippet to suit your needs.\n4. Repeat for other commands.\n5. Save as **.pm** file (Chancery sets the correct suffix for you.)\n\nAdding a command with a needle\n------------------------------\n\nIf Libvirt is running on your system and it is running in the user space, \nChancery has the ability to connect to the virtual machine and take\na screenshot of the current screen and make it into an openQA needle.\n\n1. Press **Alt-X-V** or select **VirtMachine > Connect to a VM**.\n2. Choose one of the running VMs from the drop down menu.\n3. Click the **Connect** button.\n4. Select a snippet and add it to the file.\n5. Delete the **$needlematch** place holder and leave a cursor in its place.\n6. Press **Alt-X-T** or select **VirtMachine > Create needle** to get the screenshot dialog.\n7. Set the primary tag. Note, that the needle file will be named with the tag's name.\n8. Click **Create needle** to take a screenshot of the current status quo of the virtual machine and save it as a _png_ file.\n9. Press **Alt-X-E** or select **VirtMachine > Edit needle** to open the needle in an external needle editor called Needly. If you installed Chancery with `pip`, Needly should come with it. Otherwise, install Needly with `pip install needly`.\n10. Edit the needle and save it. Read the Needly documentation for more info on how to use Needly.\n\nHow to report bugs\n==================\n\nIf you think you have found a bug, report it in the project's issues.\n",
    'author': 'Lukáš Růžička',
    'author_email': 'lruzicka@redhat.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
