/*
a) In the actor table, columns includes: actor_ID, first_name, last_name, and last_update.
b) In the film table, columns includes: film_id, title, description, release_year, language_id, original_language_id, rental_duration, rental_rate, length, replacement_cost, rating, special_features, and last_update.
c) Film actor table, columns contains both actor_id and film_id.
d) From rental table we can find which film has been rented, when was it rented, which staff rented it, who rented it, when was it returned, and the last time it was updated. It includes dates and time, customer and staff id's, inventory id and rental id. I would say it is easy to read except for the time because it is organized and clear. 
e) The inventoy table includes inventory_id, film_id, store_id, and last update. We can find information like which film was rented from which store. This also is easy to read because we can easliy get the information we are looking for. 
f) film, Inventory and rental will give us the result we are looking for. In inventory table we have film id as a foreign key which tells us the film title if we refer to film table and rental has the rental date and time.
*/

SELECT title FROM film;
SELECT rental_date FROM rental;
SELECT inventory_id FROM inventory;