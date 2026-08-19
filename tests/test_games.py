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