1. Consultas Básicas
- ¿Qué estudiantes pertenecen al área académica 'c'?
  ```sql
  SELECT * FROM academia_mega.estudiantes WHERE area_academica = 'c';
  ```
- ¿Cuántos profesores tienen especialidad en cada área?
  ```sql
    SELECT 
        E.nombre_especialidad AS especialidad,
        COUNT(PHE.id_usuario) AS cantidad_profesores
    FROM 
        ESPECIALIDADES E
    LEFT JOIN 
        PROFESORES_has_ESPECIALIDADES PHE ON E.id_especialidad = PHE.id_especialidad
    GROUP BY 
        E.nombre_especialidad
    ORDER BY 
        cantidad_profesores DESC;
  ```
- ¿Qué cursos están programados para el ciclo actual?
  ```sql
  SELECT cp.nombre_ciclo, c.nombre_curso, cc.hora_inicio, cc.hora_fin
  FROM ciclos_programados cp
  JOIN ciclos_cursos cc
  ON cp.id_ciclo = cc.id_ciclo
  JOIN cursos c
  ON cc.id_curso = c.id_curso;
  ```

- ¿Cuántos estudiantes hay inscritos en cada sede?
  ```sql
  SELECT 
    S.nombre AS sede,
    S.distrito,
    COUNT(DISTINCT E.id_usuario) AS cantidad_estudiantes,
    GROUP_CONCAT(DISTINCT CP.nombre_ciclo SEPARATOR ', ') AS ciclos_activos
  FROM 
      SEDES S
  LEFT JOIN 
      ESTUDIANTES E ON S.id_sede = E.id_sede
  LEFT JOIN 
      INSCRIPCIONES I ON E.id_usuario = I.id_usuario
  LEFT JOIN 
      CICLOS_PROGRAMADOS CP ON I.id_ciclo = CP.id_ciclo
  GROUP BY 
  	S.id_sede
  ORDER BY 
      cantidad_estudiantes DESC;
  ```

- ¿Qué profesores han tenido asistencia "tarde" en el último mes?
  ```sql
  SELECT p.nombre, p.ap_paterno, p.ap_materno, a.estado, a.fecha
  FROM profesores p
  JOIN asistencias a
  ON a.id_usuario = p.id_usuario 
  WHERE estado = "tarde" and MONTH(a.fecha) = MONTH(NOW());
  ```

2. Consultas con Joins
- Muestra el nombre completo de los estudiantes junto con el nombre de la sede donde estudian
  ```sql
  SELECT e.nombre, e.ap_paterno, e.ap_materno,
	s.nombre
  FROM estudiantes e
  JOIN inscripciones i
  ON e.id_usuario = i.id_usuario
  JOIN ciclos_programados cp
  ON i.id_ciclo = cp.id_ciclo
  JOIN sedes_ciclos sc
  ON sc.id_ciclo = cp.id_ciclo
  JOIN sedes s
  ON s.id_sede = sc.id_sede;

  ```

- Lista todos los cursos con sus respectivos profesores asignados
  ```sql
  ```

- Muestra los pagos realizados con el nombre del estudiante que los hizo
  ```sql
  ```

- ¿Qué especialidades tiene cada profesor? (muestra nombre completo del profesor y sus especialidades)
  ```sql
  ```

- Lista los grupos con su profesor asignado y el curso correspondiente
  ```sql
  ```

3. Consultas con Agregación
- ¿Cuál es el promedio de puntaje en los exámenes por área académica?
  ```sql
  ```

- ¿Cuántos estudiantes hay inscritos en cada ciclo programado?
  ```sql
  ```

- ¿Cuál es el monto total recaudado por cada sede?
  ```sql
  ```

- ¿Cuántas asistencias "ausentes" tiene cada profesor?
  ```sql
  ```

- ¿Cuál es el costo promedio de los ciclos programados por modalidad?
  ```sql
  ```

4. Consultas Avanzadas
- ¿Qué estudiantes no han rendido ningún examen?
  ```sql
  ```
- Muestra los profesores que no tienen asignado ningún grupo
  ```sql
  ```
- ¿Qué ciclos programados no tienen estudiantes inscritos?
  ```sql
  ```
- Lista los estudiantes que están inscritos en más de un ciclo
  ```sql
  ```
- Muestra los cursos que no tienen ningún grupo asignado en el ciclo actual
  ```sql
  ```
