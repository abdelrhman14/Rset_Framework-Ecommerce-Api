# Rset_Framework-Ecommerce-Api

# 1- User Registration:
    [ http://127.0.0.1:8080/rest-auth/registration/ ]

# 2- LogIn
    [ http://127.0.0.1:8080/rest-auth/login/ ] 

# 3- LogOut
    [ http://127.0.0.1:8080/rest-auth/logout/ ]

# 4- Show all Category Type:
    [ http://127.0.0.1:8080/products/category/ ]
    
# 5- Add Product Model and show it in admin
    [ http://127.0.0.1:8080/admin/ ]
    - [Admin] 
        - username : abdo
        - password : 246800#

# 6- Get Products :
- Orderd by price [ http://127.0.0.1:8080/products/category_type/<slug:slug>/ ]
EX:
    [ http://127.0.0.1:8080/products/category_type/  / ]

- Search By name: [ http://127.0.0.1:8080/products/product_filter/<slug:slug>/?name=]
EX: 
    [ http://127.0.0.1:8080/products/product_filter/  /?name=  ]

# 7- Add to cart :
    [ http://127.0.0.1:8080/products/add-to-cart/<slug:slug>/]
EX:
    [ http://127.0.0.1:8080/products/add-to-cart/  /]

# 8- Get User CArt :
    [ http://127.0.0.1:8080/products/user_cart/]

# 9- Get User Order :
    [ http://127.0.0.1:8080/products/order/]

# 10- Create New Order:
    [ http://127.0.0.1:8080/products/create_new_order/]



# Using docker and docker composed with application
 - Multi-Container Docker App
 - Python / Postgresql
 - server Django From a Container

 # CLI:
 - python -m pip freez > requirments.txt
 - docker build -t "image name" .
