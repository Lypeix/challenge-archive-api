def test_game_crud_lifecycle(client):
    create_response = client.post(
        "/games",
        json={
            "title": "Dark Souls",
            "genre": "Action RPG",
            "release_year": 2011
        }
    )

    assert create_response.status_code == 201

    created_game = create_response.json()
    game_id = created_game["id"]

    assert created_game["title"] == "Dark Souls"
    assert "created_at" in created_game

    get_response = client.get(
        f"/games/{game_id}"
    )

    assert get_response.status_code == 200
    assert get_response.json()["genre"] == "Action RPG"

    update_response = client.patch(
        f"/games/{game_id}",
        json={
            "title": "Dark Souls Remastered"
        }
    )

    assert update_response.status_code == 200
    
    updated_game = update_response.json()

    assert updated_game["title"] == "Dark Souls Remastered"

    delete_response = client.delete(
        f"/games/{game_id}"
    )

    assert delete_response.status_code == 204

    missing_response = client.get(
        f"/games/{game_id}"
    )

    assert missing_response.status_code == 404
    assert missing_response.json()["detail"] == "Game not found"

# FILTERS AND PAGINATION

def test_game_filters_and_pagination(client):
    games = [
        {
            "title": "Dark Souls",
            "genre": "Action RPG",
            "release_year": 2011
        },
        {
            "title": "Elden Ring",
            "genre": "Action RPG",
            "release_year": 2022
        },
        {
            "title": "Doom Eternal",
            "genre": "FPS",
            "release_year": 2020
        },
        {
            "title": "Tetris Effect",
            "genre": "Puzzle",
            "release_year": 2018
        }        
    ]

    for game in games:
        response = client.post(
            "/games",
            json=game
        )

        assert response.status_code == 201

    title_response = client.get(
        "/games",
        params={"title": "souls"} # equivalent to /games?title=souls
    )

    assert title_response.status_code == 200

    title_results = title_response.json()

    assert len(title_results) == 1
    assert title_results[0]["title"] == "Dark Souls"

    pagination_response = client.get(
        "/games",
        params={
            "genre": "Action RPG",
            "offset": 1,
            "limit": 1
        }
    )

    assert pagination_response.status_code == 200
    pagination_results = pagination_response.json()

    assert len(pagination_results) == 1
    assert pagination_results[0]["title"] == "Elden Ring"


def test_invalid_game_data_returns_422(client):
    response = client.post(
        "/games",
        json={
            "title": " ",
            "genre": "Action RPG",
            "release_year": 2111
        }
    )

    assert response.status_code == 422
    assert "detail" in response.json()