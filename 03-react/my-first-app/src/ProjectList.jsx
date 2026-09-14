function ProjectList({ projects}) {
    return (
        <ul>
            {projects.map((project) => (
                <li key={project}>{project}</li>
            ))}
        </ul>
    )
}

export default ProjectList