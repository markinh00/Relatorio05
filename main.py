from database import Database
from crud import Crud

db = Database(database="relatorio05", collection="livros")
db.resetDatabase()

book_crud = Crud(db)

newBookID = book_crud.creat_book("Persy Jackson", "Rick Riordan", 2005, 165.99)
book_crud.read_book_by_id(newBookID)
book_crud.update_book(newBookID, "Persy Jackson", "Rick Riordan", 2005, 100.00)
book_crud.read_book_by_id(newBookID)
book_crud.delete_book(newBookID)
