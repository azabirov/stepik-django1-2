departures = {"msk": "Москвы", "spb": "Петербурга", "nsk": "Новосибирска", "ekb": "Екатеринбурга", "kazan": "Казани", }


def statistics(request):
    return {
        'title': "Stepik Travel",
        'subtitle': "Для тех, кого отвлекают дома",
        'description': """Лучшие направления, где никто не будет
         вам мешать сидеть на берегу и изучать программирование,
        дизайн, разработку игр и управление продуктами """,
        'departures': departures.items(),
    }
