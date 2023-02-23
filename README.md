1- Registeration
[ http://127.0.0.1:8000/accounts/registration/ ]

2- Login
[ http://127.0.0.1:8000/accounts/rest-auth/login/ ]

3- Logout
[ http://127.0.0.1:8000/accounts/rest-auth/logout/ ]


4- Add Product Model and show it in admin (only) [name - price]
http://127.0.0.1:8000/admin/
username: abdo
password : 246800#

5- Get Product and the Query Shoud:
Order By Price: [ http://127.0.0.1:8000/products/category_type/slug/ ]
EX :
[ http://127.0.0.1:8000/products/category_type/mobiles-tablets/ ]

Search By Name: [http://127.0.0.1:8000/products/product_filter/slug/?name= ]
Ex :
[ http://127.0.0.1:8000/products/product_filter/mobiles-tablets/?name=Samsung Galaxy A13 ]

6 - Add To Cart: [ http://127.0.0.1:8000/products/add-to-cart/slug/ ]
Ex:
[ http://127.0.0.1:8000/products/add-to-cart/samsung-galaxy-a13/ ]
 
7- Get User Cart: [ http://127.0.0.1:8000/products/user_cart/ ]

8- Get User Orders: [ http://127.0.0.1:8000/products/order/ ]

6- Create New Order: [ http://127.0.0.1:8000/products/create_new_order/ ]

# Using docker and docker composed with application
 - Multi-Container Docker App
 - Python / Postgresql
 - server Django From a Container

 # CLI:
 - python -m pip freez > requirments.txt
 - docker build -t "image name" .
