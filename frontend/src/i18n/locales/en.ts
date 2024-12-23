export default {
  navbar: {
    home: 'Home',
    films: 'Films',
    info: {
      info: 'Information',
      locations: 'Cinemas',
      contacts: 'Contacts',
      about: 'About us',
    },
    signin: "Sign in",
    login: {
      title: "Authorization",
      google: "Google",
      microsoft: "Microsoft",
      apple: "Apple",
    },
    profile: {
      tickets: "My Tickets",
      logout: "Logout",
      admin: "Admin Panel"
    },
    lang: {
      uk: "Ukrainian",
      en: "English"
    }
  },
  pages: {
    admin: {
      menu: {
        title: "Admin Panel",
        stats: "Statistics",
        users: "Users",
        films: "Films",
        sessions: "Sessions"
      },
      stats: {
        users: "Total number of users on the platform",
        films: "Total number of films available on the platform",
        sessions: "Number of scheduled sessions in the coming days",
        tickets_sell: "Total tickets sold",
        month_money: "Revenue for the month",
        week_money: "Revenue for the week"
      },
      users: {
        give: "Grant administrator rights",
        take: "Revoke administrator rights"
      },
      films: {
        add: "Add film"
      },
      sessions: {
        add: "Add session"
      }
    },
    tickets: {
      title: "Ticket List",
      ticket: {
        session: "Session:",
        seats: "Seats:",
        download: "Download"
      }
    },
    film: {
      sessions: "Sessions",
      notsessions: "No sessions available for this film",
      buy: {
        seat: {
          title: "Seat",
          subtitle: "Choose a seat/seats"
        },
        oplata: {
          title: "Payment",
          subtitle: "Ticket payment",
          cardNumber: {
            title: "Card",
            subtitle: "Enter your card number"
          },
          cardName: {
            title: "Cardholder",
            subtitle: "Enter the cardholder's name",
            placeholder: "Name Surname"
          },
          expiryDate: {
            title: "Card expiry date",
          },
          cvv: {
            title: "CVV",
            subtitle: "3 digits on the back of the card",
            placeholder: "CVV"
          },
        },
        next: "Next",
        buy: "Pay",
        price: "$",
      },
      payment: {
        exception: {
          session_not_found: "Session not found",
          not_enough_seats: "No available seats",
          invalid_seats: "Selected seats are already taken",
          invalid_card: "Incorrect card details"
        }
      }
    },
    films: {
      title: "Film List",
      search: {
        title: "Search:",
        placeholder: "Enter keywords"
      },
      sort: {
        title: "Sort by:",
        date: "Date",
        name: "Name",
        price: "Price"
      },
      buy: "Buy",
      price: "$",
      more: "Load more",
      nomore: "You have loaded all current releases"
    },
    info: {
      about: {
        title: "KinoXata — more than just movies!",
        text1: "Our cinema is also a place to meet friends, enjoy romantic dates, or spend time with family. We often organize themed movie nights, premieres, meet-the-director events, and much more.",
        subtitle: "Our story — the way to your heart",
        text2: "KinoXata cinema started with a big dream: to create a place where every viewer would feel at home while enjoying the best cinematic moments.",
        text3: "It all started with a small hall where a group of enthusiasts showed iconic films to their closest friends. But a love for cinema and a desire to bring joy made us grow. We expanded our halls, equipped them with modern technology, and did everything to make each visit unforgettable.",
        text4: "Our logo — a cozy hut — symbolizes the warmth and comfort we want to offer every visitor. The idea to create such a cinema was born from childhood memories: how we watched movies together as a family in a small room filled with the atmosphere of unity."
      },
      contacts: {
        title: "Contacts",
        email: "kinoxata@gmail.com",
        phone: "+380000000000"
      },
      cinemas: {
        title: "Our Cinemas"
      }
    }
  },
  form: {
    successful: "Operation successful",
    noinput: "Not all fields are filled",
    add: "Add",
    edit: "Edit",
    delete: "Delete",
    close: "Close"
  }
} as const;
