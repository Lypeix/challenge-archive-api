def test_challenge_and_attempt_relationships(client):
    game_response = client.post(
        "/games",
        json={
            "title": "Dark Souls",
            "genre": "Action RPG",
            "release_year": 2011
        }
    )

    assert game_response.status_code == 201
    game_id = game_response.json()["id"]

    challenge_response = client.post(
        f"/games/{game_id}/challenges",
        json={
            "title": "Hitless Run",
            "rules": "Complete the game without getting hit at all",
            "status": "in_progress",
            "difficulty": "extreme"
        }
    )

    assert challenge_response.status_code == 201
    assert challenge_response.json()["game_id"] == game_id

    challenge = challenge_response.json()
    challenge_id = challenge["id"]

    attempt_response = client.post(
        f"/challenges/{challenge_id}/attempts",
        json={
            "result": "progressed",
            "duration_minutes": 280,
            "death_count": 0,
            "notes": "Reached Anor Londo."            
        }
    )

    assert attempt_response.status_code == 201

    attempt = attempt_response.json()
    attempt_id = attempt["id"]

    assert attempt["challenge_id"] == challenge_id

    challenges_response = client.get(
        f"/games/{game_id}/challenges"
    )

    assert challenges_response.status_code == 200

    challenges = challenges_response.json()

    assert len(challenges) == 1
    assert challenges[0]["id"] == challenge_id
    assert challenges[0]["game_id"] == game_id


    attempts_response = client.get(
        f"/challenges/{challenge_id}/attempts"
    )

    assert attempts_response.status_code == 200

    attempts = attempts_response.json()

    assert len(attempts) == 1
    assert attempts[0]["id"] == attempt_id
    assert attempts[0]["challenge_id"] == challenge_id