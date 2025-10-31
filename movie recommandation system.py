import tkinter as tk
from tkinter import messagebox
import random

# ---------------- Movie Data with Ratings ----------------
movie_data = {
    "Action": [
        ("Avengers: Endgame", 5),
        ("John Wick", 4),
        ("Iron Man", 5),
        ("The Dark Knight", 5),
        ("Fast & Furious", 3),
        ("Mad Max: Fury Road", 4),
        ("Mission Impossible", 4),
        ("Gladiator", 5)
    ],
    "Comedy": [
        ("The Mask", 4),
        ("Jumanji", 5),
        ("Home Alone", 5),
        ("The Hangover", 4),
        ("Yes Man", 3),
        ("Mr. Bean's Holiday", 4),
        ("Central Intelligence", 3)
    ],
    "Romance": [
        ("Titanic", 5),
        ("The Notebook", 5),
        ("La La Land", 4),
        ("Me Before You", 4),
        ("Dear John", 3),
        ("The Fault in Our Stars", 5),
        ("Twilight", 3)
    ],
    "Horror": [
        ("The Conjuring", 5),
        ("Annabelle", 4),
        ("IT", 4),
        ("Insidious", 3),
        ("The Nun", 3),
        ("Smile", 4)
    ],
    "Sci-Fi": [
        ("Interstellar", 5),
        ("Inception", 5),
        ("The Matrix", 5),
        ("Avatar", 4),
        ("Star Wars", 5),
        ("Dune", 4)
    ],
    "Thriller": [
        ("Gone Girl", 5),
        ("Shutter Island", 5),
        ("Se7en", 5),
        ("Prisoners", 4),
        ("Fight Club", 5),
        ("The Prestige", 4)
    ],
    "Animation": [
        ("Frozen", 4),
        ("Moana", 5),
        ("Zootopia", 4),
        ("Coco", 5),
        ("Toy Story", 4),
        ("Up", 5)
    ],
    "Drama": [
        ("Forrest Gump", 5),
        ("The Shawshank Redemption", 5),
        ("Green Book", 4),
        ("Whiplash", 5),
        ("Parasite", 5),
        ("The Social Network", 4)
    ]
}

# ---------------- Movie Recommendation Function ----------------
def recommend_movies():
    genre = genre_var.get()
    rating = rating_var.get()

    if genre == "" or rating == "":
        messagebox.showwarning("Input Error", "Please select both genre and rating!")
        return

    rating = int(rating)
    available_movies = [m for m, r in movie_data[genre] if r >= rating]

    if not available_movies:
        result_label.config(
            text="No movies found for this genre and rating.",
            fg="#ffffff", bg="#ff5252"
        )
        movie_listbox.delete(0, tk.END)
        book_btn.config(state="disabled")
    else:
        selected = random.sample(available_movies, min(3, len(available_movies)))
        result_label.config(
            text=f"Recommended Movies (Rating {rating}+):",
            fg="#222", bg="#b2f2bb"
        )

        movie_listbox.delete(0, tk.END)
        for m in selected:
            movie_listbox.insert(tk.END, m)
        book_btn.config(state="normal")

# ---------------- Ticket Booking Function ----------------
def open_booking_window():
    selected = movie_listbox.get(tk.ACTIVE)
    if not selected:
        messagebox.showerror("No Movie Selected", "Please select a movie to book.")
        return

    booking_win = tk.Toplevel(root)
    booking_win.title("Book Ticket")
    booking_win.geometry("350x300")
    booking_win.config(bg="#222831")

    tk.Label(booking_win, text=f"Book Ticket for\n{selected}", font=("Arial", 14, "bold"),
             bg="#222831", fg="#00adb5").pack(pady=20)

    tk.Label(booking_win, text="Number of Tickets:", bg="#222831", fg="#eeeeee", font=("Arial", 11)).pack(pady=5)
    ticket_entry = tk.Entry(booking_win, font=("Arial", 11))
    ticket_entry.pack(pady=5)

    tk.Label(booking_win, text="Select Show Time:", bg="#222831", fg="#eeeeee", font=("Arial", 11)).pack(pady=5)
    time_var = tk.StringVar()
    show_times = ["10:00 AM", "1:00 PM", "4:00 PM", "7:00 PM", "10:00 PM"]
    time_menu = tk.OptionMenu(booking_win, time_var, *show_times)
    time_menu.config(bg="#393e46", fg="white", width=15)
    time_menu.pack(pady=5)

    def confirm_booking():
        tickets = ticket_entry.get()
        show_time = time_var.get()
        if not tickets or not show_time:
            messagebox.showwarning("Incomplete", "Please fill all booking details.")
            return
        try:
            tickets = int(tickets)
        except:
            messagebox.showerror("Error", "Enter a valid number of tickets.")
            return
        total = tickets * 150
        messagebox.showinfo("Booking Confirmed",
                            f"Movie: {selected}\nTime: {show_time}\nTickets: {tickets}\nTotal: ₹{total}\n\nEnjoy your movie!")
        booking_win.destroy()

    tk.Button(booking_win, text="Confirm Booking", bg="#00adb5", fg="white",
              font=("Arial", 11, "bold"), width=20, command=confirm_booking).pack(pady=15)

# ---------------- GUI Setup ----------------
root = tk.Tk()
root.title("Movie Recommendation & Ticket Booking System")
root.geometry("700x700")
root.config(bg="#121212")

# ---------------- Title ----------------
title_label = tk.Label(root, text="Movie Recommendation System",
                       font=("Comic Sans MS", 20, "bold"), bg="#121212", fg="#00ffff")
title_label.pack(pady=25)

subtitle = tk.Label(root, text="Select Genre and Rating to Get Movie Suggestions",
                    font=("Arial", 12, "italic"), bg="#121212", fg="#cccccc")
subtitle.pack(pady=5)

# ---------------- Genre ----------------
genre_label = tk.Label(root, text="Choose Genre:", font=("Arial", 13, "bold"),
                       bg="#121212", fg="#ffcc00")
genre_label.pack(pady=10)

genre_var = tk.StringVar()
genres = list(movie_data.keys())
genre_menu = tk.OptionMenu(root, genre_var, *genres)
genre_menu.config(font=("Arial", 12), bg="#0097a7", fg="white", width=20, relief="ridge")
genre_menu.pack(pady=10)

# ---------------- Rating ----------------
rating_label = tk.Label(root, text="Minimum Rating:", font=("Arial", 13, "bold"),
                        bg="#121212", fg="#ffcc00")
rating_label.pack(pady=10)

rating_var = tk.StringVar()
ratings = ["3", "4", "5"]
rating_menu = tk.OptionMenu(root, rating_var, *ratings)
rating_menu.config(font=("Arial", 12), bg="#00796b", fg="white", width=10, relief="ridge")
rating_menu.pack(pady=10)

# ---------------- Recommend Button ----------------
recommend_btn = tk.Button(root, text="Recommend Movies", command=recommend_movies,
                          font=("Arial Rounded MT Bold", 13), bg="#4CAF50", fg="white",
                          width=25, relief="raised", activebackground="#81c784", cursor="hand2")
recommend_btn.pack(pady=20)

# ---------------- Result Label & Listbox ----------------
result_label = tk.Label(root, text="", font=("Arial", 14, "italic"), bg="#121212",
                        fg="#ffffff", wraplength=500, justify="center")
result_label.pack(pady=5)

movie_listbox = tk.Listbox(root, font=("Arial", 12), width=50, height=5,
                           bg="#263238", fg="white", selectbackground="#00bfa5")
movie_listbox.pack(pady=10)

# ---------------- Book Button ----------------
book_btn = tk.Button(root, text="Book Selected Movie", command=open_booking_window,
                     font=("Arial", 12, "bold"), bg="#03a9f4", fg="white",
                     width=25, relief="raised", cursor="hand2", state="disabled")
book_btn.pack(pady=15)

# ---------------- Exit & Footer ----------------
exit_btn = tk.Button(root, text="Exit", command=root.destroy, bg="#e91e63", fg="white",
                     font=("Arial", 12, "bold"), width=12, relief="ridge")
exit_btn.pack(pady=10)

footer_label = tk.Label(root, text="Developed by Muskan Rana (MCA)",
                        font=("Arial", 10, "italic"), bg="#121212", fg="#aaaaaa")
footer_label.pack(side="bottom", pady=10)

root.mainloop()
