'''
-->Special discount only if they shopped abve rs.1000.
-->Special discount applicable if and only if they are registered member.
---------------------------------------------------------------------
>If the total shopping vale is > 1000.
>If the member is a registered member.
'''

shopping_value = input('Enter the total value(in rs.):')
registered_member = input('A registered member (yes/no):').lower()

if shopping_value > 1000 and registered_member =='yes':
    print('Member is elligible for the Special Discount!')
else:
    print('Sorry your eligible for Special Discount')