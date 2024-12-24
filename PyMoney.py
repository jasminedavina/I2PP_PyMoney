import sys

class Record:
    """Represent a record."""
    def __init__(self, category, date, desc, amount):
        self._category = category
        self._date = date
        self._desc = desc
        self._amount = amount

    @property
    def category(self):
        """Make function self.category() callable by only writting self.category"""
        return self._category
    
    @property
    def date(self):
        """Make function self.date() callable by only writting self.date"""
        return self._date
    
    @property
    def desc(self):
        """Make function self.desc() callable by only writting self.desc"""
        return self._desc
    
    @property
    def amount(self):
        """Make function self.amount() callable by only writting self.amount"""
        return self._amount
    
class Records:
    value = 0
    """Maintain a list of all the 'Record's and the initial amount of money."""
    def __init__(self):
        """Get the initial amount of money and records from the source file"""
        try :
            with open('C:/Users/IdeaPad/PyMoney.txt') as fh:
                amount=fh.readline()
                self._records=list(fh.read().splitlines()) #newline character not included
                print('Welcome back!')
                self._initial_money=int(amount)
        except FileNotFoundError :
            self._records=list() 
            print('Welcome to PyMoney App!\nLet\'s begin!')
            with open('C:/Users/IdeaPad/PyMoney.txt','w+') as fh:
                while True :
                    try :
                        self._initial_money=int(input('How much money do you have? ')) #Get the original money amount
                        break
                    except ValueError :
                        sys.stderr.write('\n~ Invalid value for money.')
                        #if the inputted money format is wrong ask the user wheter re-input it or just set it to 0
                        while True :
                            choice=input('Do you want to re-input it? (Y/N)\n')
                            if choice == 'Y' :
                                self._initial_money=int(input('How much money do you have? '))
                                break
                            elif choice == 'N' :
                                money=0
                                print('~ Okay! We set it to 0 by default. But, you can edit it!\n')
                                break
                            else :
                                sys.stderr.write('~ Invalid command. Try again.\n')
                    break                           
        except :
            sys.stderr.write('~ Invalid format in PyMoney.txt. Deleting the contents.\n')
            while True :
                try :
                    amount=input('How much money do you have? ')
                    self._initial_money=int(amount)
                    break
                except ValueError :
                    sys.stderr.write('\n~ Invalid value for money.')
                    while True :
                        choice=input('Do you want to re-input it? (Y/N)\n')
                        if choice == 'Y' :
                            self._initial_money=int(input('How much money do you have? '))
                            break
                        elif choice == 'N' :
                            money=0
                            print('~ Okay! We set it to 0 by default. But, you can edit it!\n')
                            break
                        else :
                            sys.stderr.write('~ Invalid command. Try again.\n')
                break                    
            with open('C:/Users/IdeaPad/PyMoney.txt','w+') as fh:
                #clear all the file's content and also data list
                fh.truncate(0)
                fh.writelines(amount)
                self._records=list()
    
    def add(self, data, categories):
        """For adding new records to the records class"""
        record = data.split(', ')
        for idx,desc in enumerate(record):
            try :
                isi=desc.split(' ')
                #check whether the format of input is correct
                if len(isi)!=4:
                    raise IndexError
                if categories.is_category_valid(isi[0], categories._categories) != True:
                    raise AssertionError
                self._amount = int(isi[3]) #to check if the 3rd word is int or not
                self._records.append(desc) #add it to data list
                print(f'~ Succesfully adding new record(s) => {idx+1}\n~ See your updated records using \"view redords\" command!\n')
            except AssertionError :
                print(f'~ Please re-input record => {idx+1} correctly.')
                sys.stderr.write('~ The specified category is not in the category list.\
                    \n~ You can check the category list by command "view categories".\
                        \n~ Failed to add a record.\n')
            except IndexError :
                print(f'~ Please re-input record => {idx+1} correctly.')
                sys.stderr.write('~ The format of a record should be like this \"category date detail amount\".\n~ For example : meal 22/3 Breakfast -50\n~ Fail to add a record\n')   
                
            except ValueError :
                print(f'~ Please re-input record => {idx+1} correctly.')
                sys.stderr.write('~ Invalid value for money.\n~ Failed to add a record.\n')
   
    @property    
    def view(self):
        """Show the records recorded so far and also amount of money you have and can be called without adding ()"""
        money = 0
        print('Here\'s your expense and income records:')
        print('====================================================================')
        print('  No. |     Category     |   Date   |   Description   |    Amount   ')
        print('====================================================================')
        try :
            for idx, n in enumerate(self._records):
                record=n.split()
                print('{:<7} {:<22} {:<10} {:<19} {:<10}'.format(idx+1, record[0], record[1], record[2], record[3]))
                #set size column of each output
                money = money + int(record[3])
            money = money + self._initial_money
            print('====================================================================')
            print('Now you have {} dollars.'.format(money))
        except :
            #there's something wrong with the record, so the program turn into new program and the user have to re-input the record
            #if the user don't want to encounter this error, don't change any record content in the source file
            sys.stderr.write('~ Record Invalid. You have modified the records illegally.\n')
            print('~ Automatically restart your program and please re-input it!')
            with open('C:/Users/IdeaPad/PyMoney.txt','w+') as fh:
                fh.truncate(0)
            quit()
            
    @property        
    def just_view(self):
        """Just for showing the list of records so far when the user want to delete a record"""
        print('Here\'s your expense and income records:')
        print('====================================================================')
        print('  No. |     Category     |   Date   |   Description   |    Amount   ')
        print('====================================================================')
        for idx, n in enumerate(self._records):
            record=n.split()
            print('{:<10} {:<15} {:<10} {:<19} {:<10}'.format(idx+1, record[0], record[1], record[2], record[3]))
            #set size column of each output
        print('====================================================================')
    
    def delete(self, del_record):
        """Delete the record the user desired and update the list of records"""
        global value
        value=0
        try :
            hapus=del_record.split(' ')
            back=int(hapus[3])
            #check one by one each element of list 
            # if there's is one which similar to one that user want to delete, it is removed from the list
            for idx,isi in enumerate(self._records):
                if isi == del_record :
                    delete=isi.split(' ')
                    #check whether the format of input is correct
                    if len(delete) != 4 :
                        raise IndexError
                    #to know if the 3rd word is correct as an int or not
                    back=int(delete[3])
                    self._records.remove(isi)
                    value=1
                    print('~ Successfully delete the record you want!\n~ See your updated records using view command!\n')
                
            assert value==1
        except (IndexError, ValueError) :
            sys.stderr.write('~ Invalid format. Fail to delete a record.\n')
        except AssertionError : 
            sys.stderr.write(f'~ There\'s no record with {del_record}. Fail to delete a record.\n')

    def find(self, target, name):
        """Show the records under a category that the user wanted to see alongside with the total amount of money of the records"""
        amount = 0
        list_record = list(filter(lambda n : n.split()[0] in target, self._records))
        print('Here\'s your expense and income records under category "{}":'.format(name))
        print('=======================================================')
        print('  Category  |   Date   |   Description   |    Amount   ')
        print('=======================================================')
        for idx, n in enumerate(list_record):
            record=n.split()
            print('{:<15} {:<10} {:<19} {:<10}'.format(record[0], record[1], record[2], record[3]))
            #set size column of each output
            amount += int(record[3])
        print('=======================================================')
        print('The total amount above is {}.'.format(amount))

    def edit(self):
        """User can edit the records (date, desc, category, amount) or initial money"""
        global value
        value=0
        choice=input('What do you want to edit? Records (R) or Initial Money (M)\n')
        if choice == 'R' :
            #this option will delete the record that want to be edit and add the new record that editted
            self.just_view
            edit=input('Which record do you want to edit?\n')
            into=input('Change into : ')
            try :
                ubah=edit.split(' ')
                back=int(ubah[3])
                for idx,isi in enumerate(self._records):
                    if isi == edit :
                        delete=isi.split(' ')
                        back=int(delete[3])
                        self._records.remove(self._records[idx])
                    
                        isi=into.split(' ')
                        amountNum=int(isi[3])
                        self._records.insert(idx, into)
                        value=1
                        print('~ Succesfully editting the records\n~ See your updated records using \"view records\" command!\n')   
                assert value==1
            except (IndexError, ValueError) :
                sys.stderr.write('~ Invalid format. The format of a record should be like this \"date detail amount\".\n~ For example : 22/3 Breakfast -50\n~ Fail to edit a record.\n')
            except AssertionError : 
                sys.stderr.write(f'~ There\'s no record with {edit}. Fail to edit a record.\n')
        elif choice == 'M' :
            #to change the initial amount of money, not the income, 
            # for example, the original one is 1000 but user want to change it to 2000
            while True :
                try :
                    amount=input('How much money do you have? ')
                    self._initial_money=int(amount)
                    break
                except ValueError :
                    sys.stderr.write('\n~ Invalid value for money.')
                    while True :
                        choice=input('Do you want to re-input it? (Y/N)\n')
                        if choice == 'Y' :
                            break
                        elif choice == 'N' :
                            money=0
                            print('~ Okay! We set it to 0 by default. But, you can edit it!\n')
                            break
                        else :
                            sys.stderr.write('~ Invalid command. Try again.\n')
                break           
        else :
            sys.stderr.write('~ Invalid command. Try again.\n')
    
    def save(self):
        """When exiting from the program, this function will save the initial money and records to a file\
            so when you open the program again, the records inputted before is still there"""
        amount=str(self._initial_money)
        #save the amoun of money to the file and then the record is elemtn of the list, 
        # if it is the last element, don't need to add newline character
        try :
            with open('C:/Users/IdeaPad/PyMoney.txt','w') as fh:
                fh.writelines(amount)
                fh.writelines('\n')
                if len(self._records) != 0:
                    for idx,line in enumerate(self._records):
                        isi=str(line)
                        if idx<len(self._records)-1:
                            fh.writelines(isi)
                            fh.writelines('\n')
                        else :
                            fh.writelines(isi)
                        #for the last one no need to add newline character
        except :
            sys.stderr.write('~ There\'s something wrong! We can\'t save your records.\n') 
        
class Categories:
    """Maintain the category list and provide some methods."""
    def __init__(self):
        """Define the category available for this program"""
        self._categories = ['expense', 
                  ['food', ['meal', 'snack', 'drink'], 
                  'transportation', ['bus', 'railway'], 
                  'others',['laundry', 'groceries']], 
                  'income', ['salary', 'bonus']]

    def view(self, categories=None, level=-1):
        """Show the available category so the user can clearly see the level and also category"""
        if categories == None:
            categories = self._categories
        if type(categories) in {list} :
            for cat in categories :
                self.view(cat, level+1)
        else :
            print(f'{" "*level}{"-"}{categories}')

    def is_category_valid(self, target, categories=None):
        """To check if the inputted category that the user want is valid (is in the list of available category in this program or not)"""
        if categories == None:
            categories = self._categories
        if target in categories :
            return True
        else:
            for cat in categories:
                if type(cat) == list:
                    if self.is_category_valid(target, cat):
                        return True
        return False

    def find_subcategories(self, category):
        def find_subcategories_gen(category, categories, found=False):
            """When the user want to find records under a category, this function will search for its subcategory so that find function can show the records under the subcategory too"""
            if type(categories) == list:
                for index, child in enumerate(categories):
                    yield from find_subcategories_gen(category, child, found)
                    if child == category and index + 1 < len(categories) \
                        and type(categories[index + 1]) == list:
                # When the target category is found,
                # recursively call this generator on the subcategories
                # with the flag set as True.
                        yield from find_subcategories_gen(category, categories[index+1], True)
            else:
                if categories == category or found:
                    yield categories
        return list(find_subcategories_gen(category, self._categories))

categories = Categories()
records = Records()

while True:
    command = input('\nWhat do you want to do (add / view records / view categories / find / delete / edit/ exit)? \n')
    if command == 'add':
        record = input('Add some expense or income records with category, date, description, and amount (separate by spaces):\ncat1 date1 desc1 amt1, cat2 date2 desc2 amt2, cat3 date3 desc3 amt3, ...\n')
        records.add(record, categories)
    elif command == 'view records':
        records.view
    elif command == 'delete':
        records.just_view
        delete_record = input("Which record do you want to delete? ")
        records.delete(delete_record)
    elif command == 'edit' :
        records.edit()
    elif command == 'view categories':
        categories.view()
    elif command == 'find':
        category = input('Which category do you want to find? ')
        target_categories = categories.find_subcategories(category)
        records.find(target_categories, category)
    elif command == 'exit':
        records.save()
        print('Thank you for using PyMoney App!')
        break
    else:
        sys.stderr.write('Invalid command. Try again.\n')