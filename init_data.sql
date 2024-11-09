-- Insertar actividades
INSERT INTO actividades (descripcion, costo) VALUES ('snowboard', 100.00);
INSERT INTO actividades (descripcion, costo) VALUES ('ski', 120.00);
INSERT INTO actividades (descripcion, costo) VALUES ('moto de nieve', 150.00);

-- Insertar turnos
INSERT INTO turnos (hora_inicio, hora_fin) VALUES ('09:00:00', '11:00:00');
INSERT INTO turnos (hora_inicio, hora_fin) VALUES ('12:00:00', '14:00:00');
INSERT INTO turnos (hora_inicio, hora_fin) VALUES ('16:00:00', '18:00:00');

-- Insertar equipamiento
INSERT INTO equipamiento (id_actividad, descripcion, costo) VALUES (1, 'Tabla de snowboard', 50.00);
INSERT INTO equipamiento (id_actividad, descripcion, costo) VALUES (1, 'Casco de snowboard', 15.00);
INSERT INTO equipamiento (id_actividad, descripcion, costo) VALUES (1, 'Botas de snowboard', 30.00);
INSERT INTO equipamiento (id_actividad, descripcion, costo) VALUES (1, 'Guantes termicos', 10.00);
INSERT INTO equipamiento (id_actividad, descripcion, costo) VALUES (2, 'Esquis', 60.00);
INSERT INTO equipamiento (id_actividad, descripcion, costo) VALUES (2, 'Casco de ski', 15.00);
INSERT INTO equipamiento (id_actividad, descripcion, costo) VALUES (2, 'Botas de ski', 35.00);
INSERT INTO equipamiento (id_actividad, descripcion, costo) VALUES (2, 'Gafas de ski', 20.00);
INSERT INTO equipamiento (id_actividad, descripcion, costo) VALUES (3, 'Casco para moto de nieve', 20.00);
INSERT INTO equipamiento (id_actividad, descripcion, costo) VALUES (3, 'Guantes para moto de nieve', 12.00);
